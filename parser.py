import ast_nodes

class Parser:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.index = 0

    def _peek(self) -> str:
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    def _consume(self) -> str:
        token = self._peek()
        self.index += 1
        return token
    
    def _build_term(self) -> ast_nodes.ASTNode:
        left = self._build_factor()

        if self._peek() == None:
            return left
        
        while self._peek() in ("*", "/"):
            operator = self._consume()
            right = self._build_factor()

            match operator:
                case "*":
                    left = ast_nodes.Multiply(left, right)
                case "/":
                    left = ast_nodes.Divide(left, right)
                case _:
                    raise SyntaxError("Unexpected operator in term")

        return left

    def _build_expr(self) -> ast_nodes.ASTNode:
        left = self._build_term()

        if self._peek() == None:
            return left
        
        while self._peek() in ("+", "-"):
            operator = self._consume()
            right = self._build_term()

            match operator:
                case "+":
                    left = ast_nodes.Add(left, right)
                case "-":
                    left = ast_nodes.Subtract(left, right)
                case _:
                    raise SyntaxError("Unexpected operator in expr")

        return left
    
    def _build_factor(self) -> ast_nodes.ASTNode:
        if self._peek().isnumeric():
            return ast_nodes.Number(int(self._consume()))
        
        if self._consume() != "(":
            raise SyntaxError("Expected '(' in factor")

        expr = self._build_expr()

        if self._consume() != ")":
            raise SyntaxError("Expected ')' in factor")

        return expr

    def build_ast(self) -> ast_nodes.ASTNode:
        ast = self._build_expr()

        if self._peek() is not None:
            raise SyntaxError("Unexpected token after expression")

        return ast