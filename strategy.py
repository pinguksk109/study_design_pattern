from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def calculate_discount(self, total: float) -> float:
        return total
    
class TenPercentDiscount(DiscountStrategy):
    def calculate_discount(self, total: float) -> float:
        return total * 0.9
    
class TwentyDollarDiscount(DiscountStrategy):
    def calculate_discount(self, total: float) -> float:
        return max(0, total - 20)
    
class ShoppingCart:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
        self.total = 0

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def add_item(self, price: float):
        self.total += price

    def calculate_total(self) -> float:
        return self.strategy.calculate_discount(self.total)
    
cart = ShoppingCart(NoDiscount())
cart.add_item(50)
cart.add_item(100)

print("Total with no discount:", cart.calculate_total())

cart.set_strategy(TenPercentDiscount())
print("Total with 10% discount:", cart.calculate_total())

cart.set_strategy(TwentyDollarDiscount())
print("Total with $20 discount:", cart.calculate_total())