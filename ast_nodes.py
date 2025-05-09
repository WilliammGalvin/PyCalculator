class ASTNode:
    def evaluate(self) -> int:
        raise NotImplementedError("Must implement evaluate() in subclass")

class Number(ASTNode):
    def __init__(self, value: int):
        self.value = value

    def evaluate(self) -> int:
        return self.value

class Add(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()

class Subtract(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

class Multiply(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()

class Divide(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        return self.left.evaluate() / self.right.evaluate()