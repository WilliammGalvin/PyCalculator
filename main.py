import re
from parser import Parser

def tokenize_expr(input: str) -> list[str]:
    tokens = []
    
    patterns = [
        r"\d+", r"[+\-*/()]"
    ]

    while len(input) > 0:
        foundMatch = False
        input = input.lstrip()
        
        for pattern in patterns:
            match = re.match(pattern, input)

            if match:
                token = match.group(0)
                input = input[len(token):]

                foundMatch = True
                tokens.append(token)
                break
        
        if not foundMatch:
            print(f"Error determining token for input: '{input}'")
            exit(1)

    return tokens

input = "((553 + 2 - 12) * (3 * 42) / 6) - 1200"
tokens = tokenize_expr(input.strip())
ast = Parser(tokens).build_ast()
print(ast.evaluate())