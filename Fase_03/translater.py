#!/usr/bin/env python3

import random
import re
import json

# http://www.avr-asm-tutorial.net/avr_en/micro_beginner/instructions.html

FILE_NAME = "examples/exemploIo.txt"
ARDUINO_TYPE="MEGA"

## Definicoes do processador
# Definicoes de Memoria (MEGA)
MEMORY = 512
MEMORY_OCC = 2
MAX_MEM = 65535

# Determina o esquema de pinout pelo tipo do arduino
PINOUT_FILE = "arduino_defs/pinout_mega.txt"

# Verifica o tipo de arduino
if ARDUINO_TYPE == "UNO":
  PINOUT_FILE = "arduino_defs/pinout_uno.txt"
  # Definicoes de Memoria (UNO)
  MEMORY = 256
  MEMORY_OCC = 1
  MAX_MEM = 2303
  
with open(PINOUT_FILE, "r") as pinout:
  PINOUT = json.load(pinout)

## Lista de comandos
# Compara os valores de registradores
CPI = "cpi r{0}, {1}"
# Compara os valores de registradores
CP = "cp r{0}, r{1}"
# Carrega o registrador com um valor estatico
LDI = "ldi r{0}, {1}"
# Carrega um registrador com a variavel armazenada no sts
LDS = "lds r{0}, ${1}"
# Limpa o registrador
CLR = "clr r{0}"
# Pula instrucao se a comparacao for igual (==)
BREQ = "breq {0}"
# Pula instrucao se a comparacao for diferente (!=)
BRNE = "brne {0}"
# Pula instrucao se a comparacao for maior que o valor (>)
BRSH = "brsh {0}"
# Pula instrucao se a comparacao for maior ou igual ao valor (>=)
BRGE = "brge {0}"
# Pula instrucao se a comparacao for menor que o valor (<)
BRLO = "brlo {0}"
# Pula instrucao se a comparacao for menor ou igual ao valor (<=)
BRLE = "brle {0}"
# Incrementa o valor em 1
INC = "inc r{0}"
# Ou exclusivo. O valor vai para o primeiro registrador
EOR = "eor r{0}, r{1}"
# Pula para o nome
RJMP = "rjmp {0}"
# Pula a próxima instrução se o pino tiver valor 1
SBIS = "sbis PIN{0}, {1}"
# Atribui um valor a um registrador, passa para o sts e limpa o registrador
STS = "sts ${0}, r{1}"
SETUP_DIGITAL_OUTPUT_BIT_PORT = "sbi DDR{0}, {1}"
DIGITAL_OUTPUT_ON_BIT = "sbi PORT{0}, {1}"
DIGITAL_OUTPUT_OFF_BIT = "cbi PORT{0}, {1}"

SETUP_DIGITAL_INPUT_BIT_PORT = "cbi DDR{0}, {1}"

COMPARATORS = ["==", "!=", ">", ">=", "<", "<="]
COMPARATORS_BOOL = ["AND", "OR"]
REGISTER_LIST = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# Mascara para nome de metodo
METHOD_MASK = "mask_"
# Contador de metodos
METHODS = 0

## Listas de controle
# Lista do lugar das variaveis
VARIABLES = {}
# Lista da posicao de memoria das variaveis
MEM_VARIABLES = {}

## Listas de comandos
# Lista de comandos de setup
SETUP_OUTPUT_LIST = []
# Lista de comandos do corpo do codigo
OUTPUT_LIST = []
# Lista dos metodos utilizados
METHODS_OUTPUT_LIST = []


def existInInput(input, pos, value):
  return len(input) > (pos + value + 1)

# Atribui uma nova variavel
def attrNewVariable(varName, value):
  output_list = []
  # Verifica se tem espaco na memoria
  if(MEMORY < MAX_MEM):
    # Recupera um registrador disponivel
    register = availableRegister()
    # Define o registrador recebendo um valor direto
    output_list.append(LDI.format(register, value))
    
    output_list.extend(storeVariable(varName, register))
  else:
    exitWithMessage("Memoria cheia")
  return output_list

# Guarda a variavel do registrador na memoria
def storeVariable(varName, register):
  outputList = []
  global MEMORY
  varMem = None
  # Verifica se a variavel ja esta no mapa de variaveis
  if varName in MEM_VARIABLES.keys():
    # Recupera a posicao original da variavel
    varMem = MEM_VARIABLES[varName]
  else:
    # Determina uma posicao para a variavel nova
    varMem = MEMORY
    MEM_VARIABLES[varName] = varMem
    MEMORY += MEMORY_OCC
  # Formata para guardar o valor na memoria
  outputList.append(STS.format(str(hex(varMem))[2:], register))
  outputList.append(CLR.format(register))
  # Atualiza as informacoes de localizacao da variavel
  VARIABLES[varName] = "sts"
  return outputList

# Altera a variável declarada
def changeStoredVariable(varName, value):
  outputList = []
  # Recupera a variável do sts
  command, register = storageRegister(varName)
  # Adiciona o comando no retorno
  outputList.append(command)
  # Carrega a variável com o valor
  outputList.append(LDI.format(register, value))
  # Reinsere a variável no sts
  outputList.extend(storeVariable(varName, register))
  return outputList

# Retorna registrador disponivel
def availableRegister():
  newList = list(set(REGISTER_LIST) - set(VARIABLES.values()))
  return random.choice(newList)

# Retorna o comando para recuperar variavel
def storageRegister(variableName):
  # Verifica se a variavel existe
  variableName = checkVariableExists(variableName)
  # Seleciona um registrador para a variavel
  register = availableRegister()
  # Indica que a variavel esta no registrador
  VARIABLES[variableName] = register
  return LDS.format(register, str(hex(MEM_VARIABLES[variableName]))[2:]), register

# Verifica se a variavel existe
# Se for, finaliza a execucao.
def checkVariableExists(variableName):
  tmp = variableName
  if variableName.startswith("!"):
    tmp = variableName[1:]
  if tmp not in VARIABLES.keys():
    exitWithMessage(f"A Variavel {tmp} nao foi declarada")
  return tmp

# Verifica se a variavel ja esta sendo usada
# Se for, finaliza a execucao.
def checkVariableAlreadyUsed(variableName):
  if variableName in VARIABLES.keys():
    exitWithMessage(f"A Variavel {variableName} ja foi utilizada")

# Verifica se o valor e inteiro
# Se nao for, finaliza a execucao.
def checkIsInteger(value):
  if not bool(re.match("^[-+]?[0-9]+$", value)):
    exitWithMessage(f"O valor {value} nao e inteiro")
  return True

# Encerra o codigo
def exitWithMessage(message):
  print(message)
  exit(1)

# Retorna a porta e o bit que o pino representa na porta
# Encerra a execucao se o pino nao puder ser configurado
def findPinoutPortAndBit(value):
  # Inicializa os valores de retorno
  port = None
  bit = None
  # Percorre o mapeamento
  for i in PINOUT:
    # Verifica se o valor esta na lista
    if value in PINOUT[i]:
      port = i
      bit = PINOUT[i].index(value)
  if port == None or bit == None:
    exitWithMessage(f"O pino {value} nao pode ser configurado")
  return port, bit

# Verifica se o comando de configuracao ja foi inserido
# Se nao foi, insere
def insertSetupCommand(value):
  if value not in SETUP_OUTPUT_LIST:
    SETUP_OUTPUT_LIST.append(value)

# Formata um nome para método
def formatMethodName():
  global METHODS
  result = METHOD_MASK + str(METHODS)
  METHODS += 1
  return result

#######################################
# Percorre os "Tokens"
def mainLoop(input, outputList):
  pos = 0
  global METHODS_OUTPUT_LIST
  while pos < len(input):
    # Recupera o valor da posicao
    value = input[pos]
    #print(f"{pos} : {value}")
    # Declaracao de valor inteiro
    if value == "int":
      # Recupera o nome da variavel sendo declarada
      pos += 1
      variableName = input[pos]
      # Verifica se a variavel ja esta sendo usada
      checkVariableAlreadyUsed(variableName)
      # Determina valor padrao como zero
      variableValue = 0
      # Atribuicao de valor inteiro para a declaracao
      if input[pos + 1] == "=":
        pos += 1
        # Recupera o valor da atribuicao
        checkIsInteger(input[pos + 1])
        pos += 1
        variableValue = int(input[pos])
      else:
        pos += 1
      outputList.extend(attrNewVariable(variableName, variableValue))
    # Declaracao de valor booleano
    elif value == "bool":
      # Recupera o nome da variavel sendo declarada
      variableName = input[pos + 1]
      # Verifica se a variavel ja esta sendo usada
      checkVariableAlreadyUsed(variableName)
      pos += 1
      variableValue = 0
      if input[pos + 1] == "=":
        pos += 1
        # Verifica se é variável
        if checkVariableExists(input[pos + 1]):
          customVar = input[pos + 1]
          commands, register = storageRegister(customVar)
          outputList.append(commands)
          if customVar.startswith("!"):
            # Carrega registrador qualquer com 1
            oneRegister = availableRegister()
            outputList.append(LDI.format(oneRegister, 1))
            # Executa a troca do valor
            outputList.append(EOR.format(register, oneRegister))
          outputList.extend(storeVariable(variableName, register))
        else:
          # Recupera o valor da atribuicao
          if input[pos + 1] == "TRUE":
            variableValue = 1
          outputList.extend(attrNewVariable(variableName, variableValue))
      else:
        outputList.extend(attrNewVariable(variableName, variableValue))
    # Declaracao de laco condicional
    elif value == "if":
      variableName1 = input[pos + 1]
      comparator = input[pos + 2]
      variableName2 = input[pos + 3]
      ifBraceCount = 1
      i = pos + 5
      while ifBraceCount > 0 and i < len(input):
        token = input[i]
        if token == "{":
          ifBraceCount += 1
        elif token == "}":
          ifBraceCount -= 1
        i += 1
      closeBrace = i - 1
      if checkIsInteger(variableName2):
        comando, registrador1 = storageRegister(variableName1)
        outputList.append(comando)
        outputList.append(CPI.format(registrador1, variableName2))
        methodName = formatMethodName()
        retMethodName = formatMethodName()
        if comparator == "==":
          outputList.append(BREQ.format(methodName))
        elif comparator == "!=":
          outputList.append(BRNE.format(methodName))
        elif comparator == ">":
          outputList.append(BRSH.format(methodName))
        elif comparator == ">=":
          outputList.append(BRGE.format(methodName))
        elif comparator == "<":
          outputList.append(BRLO.format(methodName))
        elif comparator == "<=":
          outputList.append(BRLE.format(methodName))
        outputList.append(f"{retMethodName}:")
        METHODS_OUTPUT_LIST.append(f"{methodName}:")
        mainLoop(input[pos + 5:closeBrace], METHODS_OUTPUT_LIST)
        METHODS_OUTPUT_LIST.append(RJMP.format(retMethodName))
        METHODS_OUTPUT_LIST.append("\n")
        pos = closeBrace
      elif not checkIsInteger(variableName1) and not checkIsInteger(variableName2):
        if variableName1 not in VARIABLES or variableName2 not in VARIABLES:
          # Deve gerar erro
          print("Variaveis nao estao registradas!")
          #TODO Tratar erro
          #TODO Marcar como condicao falso
        else:
          # Nao preciso setar nenhuma
          print(f"Ambas variaveis setadas: {variableName1} e {variableName2}")
          print("Carregando as variaveis nos registradores...")
          comando, registrador1 = storageRegister(variableName1)
          outputList.append(comando)
          comando, registrador2 = storageRegister(variableName2)
          outputList.append(comando)
          outputList.append(CP.format(registrador1, registrador2))

    # Declaracao de laco de repeticao
    elif value == "for":
      variableToBeIterated = input[pos + 1]
      initialValueForVariable = input[pos + 3]
      comparator = input[pos + 6]
      finalValueForVariable = input[pos + 7]
      increment = input[pos + 12]

      forBraceCount = 1
      i = pos + 13
      while forBraceCount > 0 and i < len(input):
        token = input[i]
        if token == "{":
          forBraceCount += 1
        elif token == "}":
          forBraceCount -= 1
        i += 1
      closeBrace = i - 1

      comando, registrador = storageRegister(variableToBeIterated)
      outputList.append(comando)
      methodName = formatMethodName()
      endMethodName = formatMethodName()

      outputList.append(f"{methodName}:")
      outputList.append(CPI.format(registrador, finalValueForVariable))

      if comparator == "<":
        outputList.append(BRGE.format(endMethodName)) # Ao contrario de proposito
      
      outputList.append(INC.format(registrador))
      outputList.append(RJMP.format(methodName))

      # Ta colocando o int c = 50 no trecho principal. Tem que por na funcao de baixo...

      METHODS_OUTPUT_LIST.append(f"{endMethodName}:")
      mainLoop(input[pos + 12:closeBrace], outputList)
      METHODS_OUTPUT_LIST.append(RJMP.format(endMethodName))
      pos = closeBrace

    # Declaracao de io_output_digital
    elif value == "io_output_digital":
      pinout_value = input[pos + 1]
      value = input[pos + 2]
      # Procura o pino no mapeamento de Pinout para verificar a porta e o pino em referencia ao processador
      port, bit = findPinoutPortAndBit(pinout_value)
      # Adiciona no topo da lista de comandos de configuracao a instrucao para indicar que o pino e de saida
      insertSetupCommand(SETUP_DIGITAL_OUTPUT_BIT_PORT.format(port, bit))
      # Verifica se o valor para ser inserido no pino e uma variavel
      if value in VARIABLES.keys():
        # Recupera a variavel do sts e coloca em um registrador
        command, variable_register = storageRegister(variableName)
        outputList.append(command)
        # Assume o registrador como value
        # Compara o valor do registrador com 1 para verificar se é verdadeiro
        outputList.append(CPI.format(variable_register, 1))
        # Gera valor aleatorio para onde vai fazer Branch
        methodName = formatMethodName()
        retMethodName = formatMethodName()
        outputList.append(BREQ.format(methodName))
        outputList.append(DIGITAL_OUTPUT_OFF_BIT.format(port, bit))
        outputList.append(f"{retMethodName}:")
        METHODS_OUTPUT_LIST.append(f"{methodName}:")
        METHODS_OUTPUT_LIST.append(DIGITAL_OUTPUT_ON_BIT.format(port, bit))
        METHODS_OUTPUT_LIST.append(RJMP.format(retMethodName))
        METHODS_OUTPUT_LIST.append("\n")
      elif value == "TRUE":
        outputList.append(DIGITAL_OUTPUT_ON_BIT.format(port, bit))
      else:
        outputList.append(DIGITAL_OUTPUT_OFF_BIT.format(port, bit))
      pos += 2
    
    # Declaracao de io_input_digital
    elif value == "io_input_digital":
      pinout_value = input[pos + 1]
      variable = input[pos + 2]
      checkVariableExists(variable)
      # Procura o pino no mapeamento de Pinout para verificar a porta e o pino em referencia ao processador
      port, bit = findPinoutPortAndBit(pinout_value)
      # Adiciona no topo da lista de comandos de configuracao a instrucao para indicar que o pino e de saida
      insertSetupCommand(SETUP_DIGITAL_INPUT_BIT_PORT.format(port, bit))
      # Recupera a variavel do sts e coloca em um registrador
      variable_register = availableRegister()
      # Pula a próxima instrução se o bit estiver pressionado
      outputList.append(SBIS.format(port, bit))
      # Recupera nome do método de retorno
      methodNameRet = formatMethodName()
      # Recupera nome do método para desligar a variável
      methodNameOff = formatMethodName()
      # Pula para o método de desligar a variável
      outputList.append(RJMP.format(methodNameOff))
      METHODS_OUTPUT_LIST.append(f"{methodNameOff}:")
      # Recupera a variável do sts e Atribui o valor 0
      METHODS_OUTPUT_LIST.extend(changeStoredVariable(variable, 0))
      # Pula para o nome de retorno
      METHODS_OUTPUT_LIST.append(RJMP.format(methodNameRet))
      # Recupera nome do método para ligar a variável
      methodNameOn = formatMethodName()
      # Pula para o método de ligar a variável
      outputList.append(RJMP.format(methodNameOn))
      METHODS_OUTPUT_LIST.append(f"{methodNameOn}:")
      # Recupera a variável do sts e Atribui o valor 1
      METHODS_OUTPUT_LIST.extend(changeStoredVariable(variable, 1))
      # Pula para o nome de retorno
      METHODS_OUTPUT_LIST.append(RJMP.format(methodNameRet))
      outputList.append(f"{methodNameRet}:")
      pos += 2
    pos += 1


#######################################
# Insere as listas de comandos no arquivo de saida
def insertCommandListToOutput(file, list):
  for line in list:
    if line.startswith(METHOD_MASK):
      file.write(f"{line}\n")
    else:
      file.write(f"    {line}\n")

def readExample():
    with open(FILE_NAME, "r") as file:
      lines = file.read().replace("\n", " ")
    return lines

def main():
  global OUTPUT_LIST
  # Executa a leitura do arquivo de entrada
  # Separa a entrada por espacos
  input = readExample().split(" ")
  print(f"\nInput separado: \n{input}\n")
  mainLoop(input, OUTPUT_LIST)
  # Finalizacao
  f = open("output.txt", "w+")
  # Adiciona os comandos de configuracao
  f.write("start:\n")
  insertCommandListToOutput(f, SETUP_OUTPUT_LIST)
  f.write("main:\n")
  insertCommandListToOutput(f, OUTPUT_LIST)
  f.write("    rjmp main\n\n")
  insertCommandListToOutput(f, METHODS_OUTPUT_LIST)
  f.close()
  
if __name__ == '__main__':
  main()
