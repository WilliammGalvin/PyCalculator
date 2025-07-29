from lexer import tokenize_expr
from parser import Parser

# Our calculator input
input = "((553 + 2 - 12) * (3 * 42) / 6) - 1200"

# Lexical analysis
tokens = tokenize_expr(input.strip())
for token in tokens:
    print(token)

# Syntactical analysis and AST building
ast = Parser(tokens).build_ast()
print(ast)

# Evaluation of the AST
print(ast.evaluate())