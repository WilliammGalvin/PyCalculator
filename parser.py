import ast_nodes
from lex_token import Token, NumberToken, SymbolToken

# Parser for arithmetic expressions producing an AST
class Parser:
    # Initialize the parser with a list of tokens
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0


    # ==== Helper methods ====

    # Return the current token without consuming it, or None if at end
    def _peek(self) -> Token:
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    # Consume and return the current token, advancing the position
    def _consume(self) -> Token:
        token = self._peek()
        self.index += 1
        return token

    # Check if the current token matches the given type and optional value
    def _expect(self, token_type: type[Token], value: str = "") -> bool:
        is_instance = isinstance(self._peek(), token_type)

        if value:
            return is_instance and self._peek().value == value
        
        return is_instance
    

    # ==== Parsing methods ====

    # Parse a term: factors combined by '*' or '/' operators
    # Term ::= factor (('*' | '/') factor)* ;
    def _build_term(self) -> ast_nodes.ASTNode:
        # Start with the first factor
        left = self._build_factor()

        if self._peek() == None:
            return left
        
        
        # Continue parsing factors combined by '*' or '/' operators
        while self._expect(SymbolToken, "*") or self._expect(SymbolToken, "/"):
            operator = self._consume().value
            right = self._build_factor()

            match operator:
                case "*":
                    left = ast_nodes.Multiply(left, right)
                case "/":
                    left = ast_nodes.Divide(left, right)
                case _:
                    raise SyntaxError("Unexpected operator in term")


        # Return the left node which is now the root of this term
        return left


    # Parse an expression: terms combined by '+' or '-' operators
    # Expr ::= term (('+' | '-') term)* ;
    def _build_expr(self) -> ast_nodes.ASTNode:
        # Start with the first term
        left = self._build_term()

        if self._peek() == None:
            return left
        
        
        # Continue parsing terms combined by '+' or '-' operators
        while self._expect(SymbolToken, "+") or self._expect(SymbolToken, "-"):
            operator = self._consume().value
            right = self._build_term()

            match operator:
                case "+":
                    left = ast_nodes.Add(left, right)
                case "-":
                    left = ast_nodes.Subtract(left, right)
                case _:
                    raise SyntaxError("Unexpected operator in expr")


        # Return the left node which is now the root of this expression
        return left


    # Parse a factor: either a number or a parenthesized expression
    # Factor ::= number | '(' expr ')' ;
    def _build_factor(self) -> ast_nodes.ASTNode:
        # If the next token is a number, consume it and return a Number node
        if isinstance(self._peek(), NumberToken):
            value = int(self._consume().value)
            return ast_nodes.Number(value)
        

        # Ensure the next token is a '(' for a grouped expression
        if not self._expect(SymbolToken, "("):
            raise SyntaxError("Expected '(' in factor")

        # Consume the '('
        self._consume()

        # Build the inner expression
        expr = self._build_expr()

        # Ensure the next token is a ')' to close the group
        if not self._expect(SymbolToken, ")"):
            raise SyntaxError("Expected ')' in factor")

        # Consume the ')'
        self._consume()

        # Return the expression node
        return expr


    # Parse the entire token list and return the root of the AST
    # AST ::= expr ;
    def build_ast(self) -> ast_nodes.ASTNode:
        # Start parsing from the top-level expression
        ast = self._build_expr()

        # Ensure we have consumed all tokens
        if self._peek() is not None:
            raise SyntaxError("Unexpected token after expression")

        # Return the root of the AST
        return ast
