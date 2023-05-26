ATTR_VALUE = "ldi r{0}, {1}"
VARIABLES = {}
REGISTER = 16

input = "{ int a = 34 int b = 12315123 }"
input = input.split(" ")
pos = 0
print(input)
while pos < len(input):
    value = input[pos]
    print(f"{pos} : {value}")
    # declaração de valor inteiro
    if value == "int":
        variableName = input[pos + 1]
        # Determina valor padrão como zero
        variableValue = 0
        # Atribuição de valor inteiro para a declaração
        if input[pos + 2] == "=":
            # Recupera o valor da atribuição
            variableValue = int(input[pos + 3])
            pos += 3
        else:
            pos += 1
        print(ATTR_VALUE.format(REGISTER, variableValue))
        VARIABLES[variableName] = REGISTER
        REGISTER += 1
    pos += 1
print(VARIABLES)