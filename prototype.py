from copy import deepcopy

class Document:
    def clone(self) -> 'Document':
        raise NotImplementedError("You should implements this method!")

class ConcreteDocument(Document):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def clone(self) -> 'ConcreteDocument':
        return deepcopy(self)

    def __str__(self):
        return f"Document Title: {self.title}, Content: {self.content}"
    
def client_code() -> None:
    original_document = ConcreteDocument("Original Title", "This is the original content.")

    cloned_document = original_document.clone()

    cloned_document.title = "Cloned Title"
    cloned_document.content = "This is the cloned content."

    print(original_document)
    print(cloned_document)

client_code()