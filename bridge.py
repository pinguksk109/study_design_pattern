from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass
    
    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass

class TV(Device):
    def __init__(self):
        def __init__(self):
            self.volume = 10

    def turn_on(self) -> None:
        print('TV turned on')

    def turn_off(self) -> None:
        print('TV turned off')

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"TV volume set to {self.volume}")

class Radio(Device):
    def __init__(self):
        self.volume = 5

    def turn_on(self) -> None:
        print('Radio turned on')

    def turn_off(self) -> None:
        print('Radio turned off')

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"Radio volume set to {self.volume}")

class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self) -> None:
        self.device.turn_on()

    def turn_off(self) -> None:
        self.device.turn_off()

    def set_volume(self, volume: int) -> None:
        self.device.set_volume(volume)

class BasicRemoteControl(RemoteControl):
    pass

class AdvancedRemoteControl(RemoteControl):
    def mute(self) -> None:
        print("Muting the device")
        self.device.set_volume(0)

tv = TV()
basic_remote = BasicRemoteControl(tv)
basic_remote.turn_on()
basic_remote.set_volume(15)
basic_remote.turn_off()

radio = Radio()
advanced_remote = AdvancedRemoteControl(radio)
advanced_remote.turn_on()
advanced_remote.mute()
advanced_remote.turn_off()
