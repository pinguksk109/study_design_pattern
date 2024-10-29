from abc import ABC, abstractmethod

# Mediator
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user: 'User', message: str) -> None:
        pass

# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    def show_message(self, user: 'User', message: str) -> None:
        print(f"[{user.name}] says: {message}")

class User:
    def __init__(self, name: str, chat_room: ChatRoomMediator):
        self.name = name
        self.chat_room = chat_room

    def send_message(self, message: str) -> None:
        self.chat_room.show_message(self, message)

chat_room = ChatRoom()
user1 = User("Alice", chat_room)
user2 = User("Bob", chat_room)

user1.send_message("Hello, Bob!")
user2.send_message("Hi, Alice!")