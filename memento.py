# Memento
class TextMemento:
    def __init__(self, text: str):
        self._text = text

    def get_saved_text(self) -> str:
        return self._text

# Originator
class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str):
        self._text += text
    
    def save(self) -> TextMemento:
        return TextMemento(self._text)
    
    def restore(self, memonto: TextMemento):
        self._text = memonto.get_saved_text()

    def get_text(self) -> str:
        return self._text
    
# Caretaker
class History:
    def __init__(self):
        self._history_stack = []
    
    def push(self, memento: TextMemento):
        self._history_stack.append(memento)

    def pop(self) -> TextMemento:
        if not self._history_stack:
            return None
        return self._history_stack.pop()
    
editor = TextEditor()
history = History()

editor.write("Hello")
history.push(editor.save())
editor.write(" World")
history.push(editor.save())
editor.write("!")
history.push(editor.save())

editor.restore(history.pop())
print("After undo:", editor.get_text())

editor.restore(history.pop())
print("After another undo:", editor.get_text())

