from abc import ABC, abstractmethod

class AnimalVisitor(ABC):
    @abstractmethod
    def visit_lion(self, lion) -> None:
        pass

    @abstractmethod
    def visit_tiger(self, triger) -> None:
        pass

class FeedingVisitor(AnimalVisitor):
    def visit_lion(self, lion) -> None:
        print(f"Feeding the lion named {lion.name}")

    def visit_tiger(self, tiger) -> None:
        print(f"Feeding the triger named {tiger.name}")

class HealthCheckVisitor(AnimalVisitor):
    def visit_lion(self, lion) -> None:
        print(f"Performing a helath check on the lion named {lion.name}")

    def visit_tiger(self, tiger) -> None:
        print(f"Performing a health check on ther triger named {tiger.name}")

class Animal(ABC):
    @abstractmethod
    def accept(self, visitor: AnimalVisitor) -> None:
        pass

class Lion(Animal):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: AnimalVisitor) -> None:
        visitor.visit_lion(self)

class Tiger(Animal):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: AnimalVisitor) -> None:
        visitor.visit_tiger(self)

animals = [Lion("Simba"), Tiger("Shera")]

feeding_visitor = FeedingVisitor()
health_check_visitor = HealthCheckVisitor()

for animal in animals:
    animal.accept(feeding_visitor)
    animal.accept(health_check_visitor)