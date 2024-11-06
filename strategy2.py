from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using Credit Card {self.card_number}.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using PayPal account {self.email}.")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using Bitcoin wallet {self.wallet_address}")

class ShoppingCart:
    def __init__(self):
        self.total_amount = 0
        self.payment_strategy = None
    
    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self.payment_strategy = strategy

    def add_item(self, price: float) -> None:
        self.total_amount += price
    
    def checkout(self) -> None:
        if not self.payment_strategy:
            raise Exception("Payment strategy is not set.")
        self.payment_strategy.pay(self.total_amount)

cart = ShoppingCart()
cart.add_item(50)
cart.add_item(100)

cart.set_payment_strategy(CreditCardPayment("1234-5678-9876-5432"))
cart.checkout()

cart.set_payment_strategy(PayPalPayment("user@example.com"))
cart.checkout()

cart.set_payment_strategy(BitcoinPayment("1A2b3C4d5E6f7G8h9I0j"))
cart.checkout()