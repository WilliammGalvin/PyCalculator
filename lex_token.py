# Base class for all tokens produced by the lexer.
class Token:
    def __init__(self, value: str):
        # The raw string value of the token (e.g. '42', '+', '(', etc.)
        self.value = value


# Represents a numeric token (e.g. '42', '3', '100')
class NumberToken(Token):
    def __init__(self, value: str):
        # Calls the base Token constructor with the numeric string
        super().__init__(value)

    # Returns a string representation of the number token
    def __repr__(self) -> str:
        return f"NumberToken( {self.value} )"


# Represents a symbolic token (e.g. '+', '-', '*', '/', '(', ')')
class SymbolToken(Token):
    def __init__(self, value: str):
        # Calls the base Token constructor with the symbol character
        super().__init__(value)

    # Returns a string representation of the symbol token
    def __repr__(self) -> str:
        return f"SymbolToken( '{self.value}' )"
