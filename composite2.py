from abc import ABC, abstractmethod

class MenuComponent(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class MenuItem(MenuComponent):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def display(self) -> None:
        print(f"Item: {self.name}, Price: {self.price} yen")

class Menu(MenuComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.menu_items = []

    def add(self, component: MenuComponent) -> None:
        self.menu_items.append(component)

    def remove(self, component: MenuComponent) -> None:
        self.menu_items.remove(component)

    def display(self) -> None:
        print(f"\nMenu: {self.name}")
        print("-" * 20)
        for item in self.menu_items:
            item.display()

pizza = MenuItem("Pizza", 1000)
pasta = MenuItem("Pasta", 900)
cola = MenuItem("Cola", 300)
coffee = MenuItem("Coffee", 400)

main_menu = Menu("Main Course")
main_menu.add(pizza)
main_menu.add(pasta)

drink_menu = Menu("Drinks")
drink_menu.add(cola)
drink_menu.add(coffee)

full_menu = Menu("Full Menu")
full_menu.add(main_menu)
full_menu.add(drink_menu)

full_menu.display()