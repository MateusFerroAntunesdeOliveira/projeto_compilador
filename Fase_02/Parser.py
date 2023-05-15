#!/usr/bin/env python3

import antlr4
import sys
from numParserLexer import numParserLexer
from numParserParser import numParserParser

fileName = "exemplos/exemplo1.txt";

if len(sys.argv) > 1:
    fileName = sys.argv[1]

print(f"Arquivo sendo testado: {fileName}\n\n")

# Crie um stream de caracteres a partir do código-fonte
input_stream = antlr4.FileStream(fileName)

# Crie um lexer a partir do stream de caracteres
lexer = numParserLexer(input_stream)

# Crie um stream de tokens a partir do lexer
token_stream = antlr4.CommonTokenStream(lexer)

# Crie um parser a partir do stream de tokens
parser = numParserParser(token_stream)

# Chame a regra de produção inicial do seu arquivo.g4
tree = parser.program()

# Imprima a árvore de análise sintática gerada
print(tree.toStringTree())
