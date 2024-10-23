from abc import ABC, abstractmethod

# 抽象クラス: Button
class Button(ABC):
    @abstractmethod
    def click(self) -> None:
        pass

# 抽象クラス: TextField
class TextField(ABC):
    @abstractmethod
    def type_text(self, text: str) -> None:
        pass

# 具体クラス: WindowsButton
class WindowsButton(Button):
    def click(self) -> None:
        print("Windows Button clicked!")

# 具体クラス: WindowsTextField
class WindowsTextField(TextField):
    def type_text(self, text: str) -> None:
        print(f"Typing in Windows TextField: {text}")

# 具体クラス: MacButton
class MacButton(Button):
    def click(self) -> None:
        print("Mac Button clicked!")

# 具体クラス: MacTextField
class MacTextField(TextField):
    def type_text(self, text: str) -> None:
        print(f"Typing in Mac TextField: {text}")

# 抽象ファクトリ: UIFactory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_text_field(self) -> TextField:
        pass

# 具体ファクトリ: WindowsUIFactory
class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_text_field(self) -> TextField:
        return WindowsTextField()

# 具体ファクトリ: MacUIFactory
class MacUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_text_field(self) -> TextField:
        return MacTextField()

# クライアントコード
def client_code(factory: UIFactory) -> None:
    button = factory.create_button()
    text_field = factory.create_text_field()
    
    button.click()
    text_field.type_text("Hello, Abstract Factory!")

# WindowsのUIコンポーネントを生成する
print("Windows UI:")
windows_factory = WindowsUIFactory()
client_code(windows_factory)

# MacのUIコンポーネントを生成する
print("\nMac UI:")
mac_factory = MacUIFactory()
client_code(mac_factory)
