from abc import ABC, abstractmethod

# Context: 数式のコンテキストを保持
class MathContext:
    def __init__(self, expression: str):
        self.expression = expression

# Abstract Expression: 数式の解釈を行うインターフェース
class MathExpression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass

# Terminal Expression: 数字をそのまま評価するクラス
class NumberExpression(MathExpression):
    def __init__(self, number: int):
        self.number = number

    def interpret(self) -> int:
        return self.number

# Non-terminal Expression: 足し算の解釈を行うクラス
class AddExpression(MathExpression):
    def __init__(self, left: MathExpression, right: MathExpression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()

# Non-terminal Expression: 引き算の解釈を行うクラス
class SubtractExpression(MathExpression):
    def __init__(self, left: MathExpression, right: MathExpression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()

# クライアントコード: 数式を解析し、計算を実行
def parse_expression(expression: str) -> MathExpression:
    tokens = expression.split()
    stack = []
    
    for token in tokens:
        if token.isdigit():
            # 数字はNumberExpressionとして評価スタックに積む
            stack.append(NumberExpression(int(token)))
        elif token == "+":
            # スタックから2つの要素を取得しAddExpressionで評価
            right = stack.pop()
            left = stack.pop()
            stack.append(AddExpression(left, right))
        elif token == "-":
            # スタックから2つの要素を取得しSubtractExpressionで評価
            right = stack.pop()
            left = stack.pop()
            stack.append(SubtractExpression(left, right))

    return stack.pop()

# 使用例: "5 + 3 - 2"の数式を解釈
expression = "5 + 3 - 2"
parsed_expression = parse_expression(expression)
result = parsed_expression.interpret()

print(f"{expression} = {result}")  # 出力: "5 + 3 - 2 = 6"
