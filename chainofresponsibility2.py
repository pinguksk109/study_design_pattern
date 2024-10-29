from abc import ABC, abstractmethod
from typing import Optional

# Abstract Handler: バリデーションの基底クラス
class Validator(ABC):
    def __init__(self, next_validator: Optional["Validator"] = None):
        self._next_validator = next_validator

    @abstractmethod
    def validate(self, data: dict) -> bool:
        pass

    def next(self, data: dict) -> bool:
        if self._next_validator:
            return self._next_validator.validate(data)
        return True

# Concrete Handlers: 各バリデーションルール
class RequiredFieldValidator(Validator):
    def validate(self, data: dict) -> bool:
        if not data.get("username"):
            print("Error: 'username' is required.")
            return False
        return self.next(data)

class EmailValidator(Validator):
    def validate(self, data: dict) -> bool:
        email = data.get("email", "")
        if "@" not in email or "." not in email:
            print("Error: 'email' is not in a valid format.")
            return False
        return self.next(data)

class PasswordStrengthValidator(Validator):
    def validate(self, data: dict) -> bool:
        password = data.get("password", "")
        if len(password) < 8:
            print("Error: 'password' must be at least 8 characters long.")
            return False
        return self.next(data)

# バリデーションのチェーンを作成
password_validator = PasswordStrengthValidator()
email_validator = EmailValidator(password_validator)
required_field_validator = RequiredFieldValidator(email_validator)

# クライアントコード
def client_code(validator: Validator, form_data: dict):
    if validator.validate(form_data):
        print("All validations passed.")
    else:
        print("Validation failed.")

# 検証するデータ
form_data = {
    "username": "john_doe",
    "email": "john.doe@example",
    "password": "pass123"
}

client_code(required_field_validator, form_data)
