from abc import ABC, abstractmethod

# Mediator interface
class SmartHomeMediator(ABC):
    @abstractmethod
    def notify(self, sender: 'Device', event: str) -> None:
        pass

# Concrete Mediator
class SmartHomeHub(SmartHomeMediator):
    def __init__(self):
        self.light = None
        self.air_conditioner = None
        self.music_player = None

    def set_light(self, light: 'Light'):
        self.light = light

    def set_air_conditioner(self, air_conditioner: 'AirConditioner'):
        self.air_conditioner = air_conditioner

    def set_music_player(self, music_player: 'MusicPlayer'):
        self.music_player = music_player

    def notify(self, sender: 'Device', event: str) -> None:
        if event == "night_mode":
            print("\nNight mode activated.")
            self.light.turn_off()
            self.air_conditioner.set_temperature(18)
            self.music_player.stop_music()
        elif event == "morning_mode":
            print("\nMorning mode activated.")
            self.light.turn_on()
            self.air_conditioner.set_temperature(22)
            self.music_player.play_music("morning playlist")

# Colleague (各デバイスの基本クラス)
class Device:
    def __init__(self, mediator: SmartHomeMediator):
        self.mediator = mediator

# Concrete Colleague (個々のデバイス)
class Light(Device):
    def turn_on(self):
        print("Light: Turning on.")

    def turn_off(self):
        print("Light: Turning off.")

class AirConditioner(Device):
    def set_temperature(self, temperature: int):
        print(f"Air Conditioner: Setting temperature to {temperature}°C.")

class MusicPlayer(Device):
    def play_music(self, playlist: str):
        print(f"Music Player: Playing {playlist}.")

    def stop_music(self):
        print("Music Player: Stopping music.")

# 利用例
hub = SmartHomeHub()
light = Light(hub)
air_conditioner = AirConditioner(hub)
music_player = MusicPlayer(hub)

# Hubにデバイスをセット
hub.set_light(light)
hub.set_air_conditioner(air_conditioner)
hub.set_music_player(music_player)

# デバイスのモード設定
hub.notify(light, "night_mode")
hub.notify(light, "morning_mode")
