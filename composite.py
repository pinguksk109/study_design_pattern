from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, intent: str = "") -> None:
        pass


class File(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
    
    def display(self, indent: str = "") -> None:
        print(f"{indent}- File: {self.name}")

class Directory(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []
    
    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        self.children.remove(component)

    def display(self, indent: str = "") -> None:
        print(f"{indent}+ Directory: {self.name}")
        for child in self.children:
            child.display(indent + "  ")

root = Directory("root")
home = Directory("home")
user = Directory("user")
docs = Directory("docs")

file1 = File("file1.txt")
file2 = File("file2.txt")
file3 = File("file3.txt")

docs.add(file1)
docs.add(file2)
user.add(docs)
user.add(file3)
home.add(user)
root.add(home)

root.display()