from abc import ABC, abstractmethod
from typing import Optional

class Logger(ABC):
    def __init__(self, next_handler: Optional["Logger"] = None):
        self._next_handler = next_handler

    @abstractmethod
    def log(self, message: str, level: str) -> None:
        pass

    def next(self, message: str, level: str) -> None:
        if self._next_handler:
            self._next_handler.log(message, level)

class DebugLogger(Logger):
    def log(self, message: str, level: str) -> None:
        if level == "DEBUG":
            print(f"[DEBUG] {message}")
        else:
            self.next(message, level)

class InfoLogger(Logger):
    def log(self, message: str, level: str) -> None:
        if level == "INFO":
            print(f"[INFO] {message}")
        else:
            self.next(message, level)

class ErrorLogger(Logger):
    def log(self, message: str, level: str) -> None:
        if level == "ERROR":
            print(f"[ERROR] {message}")
        else:
            self.next(message, level)

error_logger = ErrorLogger()
info_logger = InfoLogger(error_logger)
debug_logger = DebugLogger(info_logger)

def client_code(logger: Logger):
    logger.log("This is a debug message", "DEBUG")
    logger.log("This is an info message", "INFO")
    logger.log("This is an error message", "ERROR")
    logger.log("This is an unknown message", "UNKNOWN")

client_code(debug_logger)