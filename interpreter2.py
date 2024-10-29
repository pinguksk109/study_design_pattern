from abc import ABC, abstractmethod

# Context: 解析の文脈（ログメッセージのデータや条件を保持する）
class LogContext:
    def __init__(self, log_message: str):
        self.log_message = log_message

# Abstract Expression: すべての式の共通インターフェース
class LogExpression(ABC):
    @abstractmethod
    def interpret(self, context: LogContext) -> bool:
        pass

# Terminal Expression: エラーログを解析するクラス
class ErrorLogExpression(LogExpression):
    def interpret(self, context: LogContext) -> bool:
        return "ERROR" in context.log_message

# Terminal Expression: 警告ログを解析するクラス
class WarningLogExpression(LogExpression):
    def interpret(self, context: LogContext) -> bool:
        return "WARNING" in context.log_message

# Terminal Expression: 情報ログを解析するクラス
class InfoLogExpression(LogExpression):
    def interpret(self, context: LogContext) -> bool:
        return "INFO" in context.log_message

# Non-terminal Expression: 特定の2つの条件を組み合わせるクラス
class AndExpression(LogExpression):
    def __init__(self, expr1: LogExpression, expr2: LogExpression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: LogContext) -> bool:
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# クライアントコード: 条件に基づいてログを解析する
def log_filter(log_message: str, expression: LogExpression) -> bool:
    context = LogContext(log_message)
    return expression.interpret(context)

# 使用例: エラーログをフィルタリング
error_expression = ErrorLogExpression()
print(log_filter("ERROR: Disk space low", error_expression))  # 出力: True
print(log_filter("INFO: System started", error_expression))   # 出力: False

# 使用例: エラーかつ警告が含まれるログをフィルタリング
error_and_warning_expression = AndExpression(ErrorLogExpression(), WarningLogExpression())
print(log_filter("ERROR: Disk space low WARNING: High memory usage", error_and_warning_expression))  # 出力: True
print(log_filter("ERROR: Disk space low", error_and_warning_expression))                            # 出力: False
