# Base class for all AST (Abstract Syntax Tree) nodes.
class ASTNode:
    # Evaluates the expression represented by this node and returns its value.
    def evaluate(self) -> int:
        pass


# Represents a numeric literal (e.g. 42)
class Number(ASTNode):
    def __init__(self, value: int):
        self.value = value

    # Returns the numeric value directly.
    def evaluate(self) -> int:
        pass

    # Returns a formatted string of the number node.
    def __repr__(self) -> str:
        return f"Number( {self.value} )"


# Represents an addition operation (e.g. a + b)
class Add(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left    # Left operand (can be any AST node)
        self.right = right  # Right operand

    # Recursively evaluates the left and right sides and adds the results.
    def evaluate(self) -> int:
        pass

    # Returns a formatted string of the addition node and its children.
    def __repr__(self) -> str:
        return f"Add( {self.left}, {self.right} )"


# Represents a subtraction operation (e.g. a - b)
class Subtract(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    # Evaluates the subtraction of right from left.
    def evaluate(self) -> int:
        pass

    # Returns a formatted string of the subtraction node and its children.
    def __repr__(self) -> str:
        return f"Subtract( {self.left}, {self.right} )"


# Represents a multiplication operation (e.g. a * b)
class Multiply(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    # Returns the product of the left and right evaluations.
    def evaluate(self) -> int:
        pass

    # Returns a formatted string of the multiplication node.
    def __repr__(self) -> str:
        return f"Multiply( {self.left}, {self.right} )"


# Represents a division operation (e.g. a / b)
class Divide(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    # Performs floating-point division of the evaluated left and right nodes.
    def evaluate(self) -> int:
        pass
    
    # Returns a formatted string of the division node.
    def __repr__(self) -> str:
        return f"Divide( {self.left}, {self.right} )"
    