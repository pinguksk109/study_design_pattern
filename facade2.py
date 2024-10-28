class ProductRepository:
    def get_product(self, product_id: int) -> str:
        return f"Product {product_id}"

class InventoryRepository:
    def check_stock(self, product_id: int) -> bool:
        print(f"Checking stock for product {product_id}")
        return True
    
    def reduce_stock(self, product_id: int) -> None:
        print(f"Reducing stock for product {product_id}")

class UserRepository:
    def get_user(self, user_id: int) -> str:
        return f"User {user_id}"
    
class OrderService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.inventory_repository = InventoryRepository()
        self.user_repository = UserRepository()

    def place_order(self, user_id: int, product_id: int) -> None:
        user = self.user_repository.get_user(user_id)
        print(f"Retrieved {user}")

        product = self.product_repository.get_product(product_id)
        print(f"Retrieved {product}")

        if self.inventory_repository.check_stock(product_id):
            self.inventory_repository.reduce_stock(product_id)
            print(f"Order placed successfully for {user} with {product}")
        else:
            print("Sorry, the product is out of stock.")
