class Font:
    def __init__(self, family: str, size: int, color: str):
        self.family = family
        self.size = size
        self.color = color
    
class FontFactory:
    _fonts = {}

    @classmethod
    def get_font(cls, family: str, size: int, color: str):
        key = (family, size, color)
        if key not in cls._fonts:
            cls._fonts[key] = Font(family, size, color)
        return cls._fonts[key]

class Character:
    def __init__(self, char: str, font: Font, x: int, y: int):
        self.char = char
        self.font = font 
        self.x = x
        self.y = y

    def display(self):
        print(f"Displaying '{self.char}' at ({self.x}, {self.y}) "
              f"with font: {self.font.family}, size: {self.font.size}, color: {self.font.color}")

def render_text():
    factory = FontFactory()

    font = factory.get_font("Arial", 12, "Black")

    characters = [
        Character('H', font, 0, 0),
        Character('e', font, 10, 0),
        Character('l', font, 20, 0),
        Character('l', font, 30, 0),
        Character('o', font, 40, 0)
    ]

    for char in characters:
        char.display()

render_text()