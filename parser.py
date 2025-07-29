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
        return None

    # Consume and return the current token, advancing the position
    def _consume(self) -> Token:
        return None

    # Check if the current token matches the given type and optional value
    def _expect(self, token_type: type[Token], value: str = "") -> bool:
        return False
    

    # ==== Parsing methods ====

    # Parse a term: factors combined by '*' or '/' operators
    # Term ::= factor (('*' | '/') factor)* ;
    def _build_term(self) -> ast_nodes.ASTNode:
        return None


    # Parse an expression: terms combined by '+' or '-' operators
    # Expr ::= term (('+' | '-') term)* ;
    def _build_expr(self) -> ast_nodes.ASTNode:
        return None


    # Parse a factor: either a number or a parenthesized expression
    # Factor ::= number | '(' expr ')' ;
    def _build_factor(self) -> ast_nodes.ASTNode:
        return None


    # Parse the entire token list and return the root of the AST
    # AST ::= expr ;
    def build_ast(self) -> ast_nodes.ASTNode:
        return None
