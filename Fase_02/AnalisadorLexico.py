# Mapeamentos
letter = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "_", "-"
]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
keywords = [
    "if", "elseif", "else", "for", "return", "break", "null", "int", "float",
    "boolean", "void", "TRUE", "FALSE", "io_input_digital", "io_output_digital",
    "io_input_analog", "io_output_analog"
]
operator = ["+", "-", "*", "/", "%", "exp"]
logical_operator = ["OR", "AND", "!"]
comparator = ["<", "<=", ">", ">=", "==", "!="]
attr = ["="]
separator = ["."]
parentheses = ["(", ")"]
braces = ["{", "}"]
semicolon = [";"]
comma = [","]

arq = ["./exemplos/exemplo1.txt", "./exemplos/exemplo2.txt", "./exemplos/exemplo3.txt"]

def lexical_analysis(source_code):
    tokens = []
    i = 0
    while i < len(source_code):
        c = source_code[i]
        if c in letter:
            # identificador ou palavra-chave
            lexeme = ""
            while i < len(source_code) and source_code[i] in letter + num:
                lexeme += source_code[i]
                i += 1
            if lexeme in keywords:
                tokens.append(("KEYWORD", lexeme))
            else:
                tokens.append(("IDENTIFIER", lexeme))
        elif c in num:
            # número
            lexeme = ""
            while i < len(source_code) and source_code[i] in num:
                lexeme += source_code[i]
                i += 1
            tokens.append(("NUMBER", lexeme))
        elif c in operator:
            tokens.append(("OPERATOR", c))
            i += 1
        elif c in comparator:
            lexeme = c
            if i < len(source_code) - 1 and source_code[i:i + 2] in comparator:
                lexeme = source_code[i:i + 2]
                i += 2
            else:
                i += 1
            tokens.append(("COMPARATOR", lexeme))
        elif c in logical_operator:
            lexeme = c
            if i < len(source_code) - 1 and source_code[i:i + 2] in logical_operator:
                lexeme = source_code[i:i + 2]
                i += 2
            else:
                i += 1
            tokens.append(("LOGICAL_OPERATOR", lexeme))
        elif c in attr:
            tokens.append(("ATTR", c))
            i += 1
        elif c in separator:
            tokens.append(("SEPARATOR", c))
            i += 1
        elif c in parentheses:
            tokens.append(("PARENTHESES", c))
            i += 1
        elif c in braces:
            tokens.append(("BRACES", c))
            i += 1
        elif c in semicolon:
            tokens.append(("SEMICOLON", c))
            i += 1
        elif c in comma:
            tokens.append(("COMMA", c))
            i += 1
        elif c.isspace():
            # ignora espaços em branco
            i += 1
        else:
            tokens.append(("error", c))
            i += 1
            #raise Exception("Not a valid character")
    return tokens

for arquivo in arq:
    with open(arquivo, "r") as f:
        source_code = f.read()

    tokens = lexical_analysis(source_code)
    for token in tokens:
        print(token)
    print("\n\n")
