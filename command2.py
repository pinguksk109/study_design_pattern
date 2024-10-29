from abc import ABC, abstractmethod

# Commandの抽象クラス
class OrderCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# Receiver: シェフが実際に調理を担当
class Chef:
    def prepare_pasta(self) -> None:
        print("Chef is preparing pasta...")
    
    def prepare_steak(self) -> None:
        print("Chef is preparing steak...")

# Concrete Command: Pastaの注文
class PastaOrderCommand(OrderCommand):
    def __init__(self, chef: Chef):
        self.chef = chef

    def execute(self) -> None:
        self.chef.prepare_pasta()

# Concrete Command: Steakの注文
class SteakOrderCommand(OrderCommand):
    def __init__(self, chef: Chef):
        self.chef = chef

    def execute(self) -> None:
        self.chef.prepare_steak()

# Invoker: ウェイターが注文をキッチンに伝える役割
class Waiter:
    def __init__(self):
        self.command_queue = []

    def take_order(self, command: OrderCommand) -> None:
        self.command_queue.append(command)

    def send_orders(self) -> None:
        for command in self.command_queue:
            command.execute()
        self.command_queue.clear()

# 利用例
chef = Chef()
pasta_order = PastaOrderCommand(chef)
steak_order = SteakOrderCommand(chef)

waiter = Waiter()
waiter.take_order(pasta_order)   # パスタの注文を受ける
waiter.take_order(steak_order)   # ステーキの注文を受ける

waiter.send_orders()
# 出力:
# Chef is preparing pasta...
# Chef is preparing steak...
