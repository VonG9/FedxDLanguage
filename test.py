code = open("basic.py", "r").read()

replacers = {
    "VAR": "let",
    "FUN": "fex",
    "AND": "and",
    "OR": "or",
    "NOT": "not",
    "IF": "if",
    "ELIF": "elif",
    "ELSE": "else",
    "WHILE": "while",
    "FOR": "for",
    "TO": "to",
    "STEP": "step",
    "THEN": "then",
    "NULL": "Null",
    "TRUE": "True",
    "FALSE": "False",
    "END": "end",
    "RETURN": "return",
    "CONTINUE": "continue",
    "BREAK": "break",
}

for key, value in replacers.items():
    code = code.replace(f"'{key}'", f"'{value}'")

with open("basic.py", "w") as file:
    file.write(code)
