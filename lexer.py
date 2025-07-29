from lex_token import Token, NumberToken, SymbolToken

# Tokenize a mathematical expression string into a list of tokens
def tokenize_expr(input: str) -> list[Token]:
    # Initalize an empty list to hold tokens
    tokens = []

    # Loop through the input string character by character
    while len(input) > 0:
        # Strip leading whitespace
        input = input.lstrip()

        # Peek first character
        peek = input[0]

        # Check if peek is a symbol and add it as a SymbolToken
        if peek in "+-*/()":
            tokens.append(SymbolToken(peek))
            input = input[1:]
            continue
        

        # Check if peek is a digit and parse the full number
        num = ""
        while len(input) > 0 and input[0].isdigit():
            num += input[0]
            input = input[1:]


        # If we found a number, create a NumberToken
        if num:
            tokens.append(NumberToken(num))
            continue
        

        # If we reach here, it means we encountered an unexpected character
        print(f"Error determining token for input: '{input}'")
        exit(1)


    # Return the list of tokens
    return tokens
