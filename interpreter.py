from abc import ABC, abstractmethod

class Context:
    def __init__(self, expression: str):
        self.expression = expression.split()
        self.index = 0
        
    def next_token(self) -> str:
        token = self.expression[self.index]
        self.index += 1
        return token

class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> int:
        pass

class NumberExpression(Expression):
    def __init__(self, number: int):
        self.number = number

    def interpret(self, context: Context) -> int:
        return self.number

class AddExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) + self.right.interpret(context)
    
class SubstractExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) - self.right.interpret(context)
    
def parse_expression(context: Context) -> Expression:
    left = NumberExpression(int(context.next_token()))
    operator = context.next_token()
    right = NumberExpression(int(context.next_token()))

    if operator == '+':
        return AddExpression(left, right)
    elif operator == '-':
        return SubstractExpression(left, right)
    else:
        raise ValueError("Invalid operator")
    
context = Context("5 + 3")
expression = parse_expression(context)
result = expression.interpret(context)
print(result)

context = Context("10 - 7")
expression = parse_expression(context)
result = expression.interpret(context)
print(result)