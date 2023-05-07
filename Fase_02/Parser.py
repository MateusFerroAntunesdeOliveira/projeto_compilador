import antlr4
from ParserLexer import ParserLexer
from ParserParser import ParserParser

# Crie um stream de caracteres a partir do código-fonte
input_stream = antlr4.FileStream("exemplos/exemplo3.txt")

# Crie um lexer a partir do stream de caracteres
lexer = ParserLexer(input_stream)

# Crie um stream de tokens a partir do lexer
token_stream = antlr4.CommonTokenStream(lexer)

# Crie um parser a partir do stream de tokens
parser = ParserParser(token_stream)

# Chame a regra de produção inicial do seu arquivo.g4
tree = parser.program()

# Imprima a árvore de análise sintática gerada
print(tree.toStringTree())
