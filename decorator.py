from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def send(self, content: str) -> None:
        pass

class SimpleMessage(Message):
    def send(self, content: str) -> None:
        print(f"SimpleMessage: {content}")

class MessageDecorator(Message):
    def __init__(self, message: Message) -> None:
        self._message = message

    def send(self, content: str) -> None:
        self._message.send(content)

class LoggedMessage(MessageDecorator):
    def send(self, content: str) -> None:
        print(f"LoggedMessage: {content}")
        super().send(content)

class EncryptedMessage(MessageDecorator):
    def send(self, content: str) -> None:
        encrypted_content = self._encrypt(content)
        print(f"Encrypted content: {encrypted_content}")
        super().send(encrypted_content)

    def _encrypt(self, content: str) -> str:
        return ''.join(chr(ord(char) + 1) for char in content)
    
simple_message = SimpleMessage()
simple_message.send("Hello, World!")

logged_message = LoggedMessage(simple_message)
logged_message.send("Hello")

encrypted_message = EncryptedMessage(simple_message)
encrypted_message.send("Hello")

logged_encrypted_message = LoggedMessage(EncryptedMessage(simple_message))
logged_encrypted_message.send("Hello")