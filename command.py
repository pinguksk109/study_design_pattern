from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class Light:
    def turn_on(self) -> None:
        print("Light is ON")

    def turn_off(self) -> None:
        print("Light is OFF")

class TurnOnLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

class TurnOffLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command) -> None:
        self.command = command

    def press_button(self) -> None:
        if self.command:
            self.command.execute()

light = Light()
turn_on_command = TurnOnLightCommand(light)
turn_off_command = TurnOffLightCommand(light)

remote = RemoteControl()
remote.set_command(turn_on_command)
remote.press_button()

remote.set_command(turn_off_command)
remote.press_button()