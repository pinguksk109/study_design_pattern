class Pizza:
    def __init__(self, size: str, cheese: bool, pepperoni: bool, mushrooms: bool):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
    
    def __str__(self):
        return (f"Pizza(size={self.size}, cheese={self.cheese}, "
                f"pepperoni={self.pepperoni}, mushrooms={self.mushrooms})")
    
class PizzaBuilder:
    def __init__(self):
        self.size = "Medium"
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
    
    def set_size(self, size: str) -> 'PizzaBuilder':
        self.size = size
        return self
     
    def add_cheese(self) -> 'PizzaBuilder':
        self.cheese = True
        return self

    def add_pepperoni(self) -> 'PizzaBuilder':
        self.pepperoni = True
        return self

    def add_mushrooms(self) -> 'PizzaBuilder':
        self.mushrooms = True
        return self

    def build(self) -> Pizza:
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms)

def client_code() -> None:
    builder = PizzaBuilder()

    pizza = (builder.set_size("Large").add_cheese().add_pepperoni().build())

    print(pizza)

client_code()