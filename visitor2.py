from abc import ABC, abstractmethod

# Visitor: 操作のインターフェース
class StoreVisitor(ABC):
    @abstractmethod
    def visit_electronics_store(self, electronics_store) -> None:
        pass

    @abstractmethod
    def visit_clothing_store(self, clothing_store) -> None:
        pass

# Concrete Visitor: 在庫チェックの実施
class InventoryCheckVisitor(StoreVisitor):
    def visit_electronics_store(self, electronics_store) -> None:
        print(f"Checking inventory at {electronics_store.name}")

    def visit_clothing_store(self, clothing_store) -> None:
        print(f"Checking inventory at {clothing_store.name}")

# Concrete Visitor: プロモーションの実施
class PromotionVisitor(StoreVisitor):
    def visit_electronics_store(self, electronics_store) -> None:
        print(f"Running a promotion at {electronics_store.name}")

    def visit_clothing_store(self, clothing_store) -> None:
        print(f"Running a promotion at {clothing_store.name}")

# Element: 店舗の基本クラス
class Store(ABC):
    @abstractmethod
    def accept(self, visitor: StoreVisitor) -> None:
        pass

# Concrete Element: 電子機器店
class ElectronicsStore(Store):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: StoreVisitor) -> None:
        visitor.visit_electronics_store(self)

# Concrete Element: 衣料品店
class ClothingStore(Store):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: StoreVisitor) -> None:
        visitor.visit_clothing_store(self)

# Object Structure: 店舗のリスト
stores = [ElectronicsStore("Best Electronics"), ClothingStore("Fashion Hub")]

# Visitor の使用例
inventory_visitor = InventoryCheckVisitor()
promotion_visitor = PromotionVisitor()

for store in stores:
    store.accept(inventory_visitor)  # 各店舗で在庫チェックを実施
    store.accept(promotion_visitor)  # 各店舗でプロモーションを実施
