class Projector:
    def on(self) -> None:
        print("Projector is turned on.")

    def off(self) -> None:
        print("Projector is turned off")

class SoundSystem:
    def on(self) -> None:
        print("Sound system is turned on.")

    def set_volume(self, level: int) -> None:
        print(f"Setting sound system volume to {level}.")

    def off(self) -> None:
        print("Sound system is turned off.")

class StreamingService:
    def connect(self) -> None:
        print("Connected to streaming service.")

    def disconnect(self) -> None:
        print("Disconnected from streaming service.")

    def play_movie(self, title: str) -> None:
        print(f"Playing movie '{title}'.")

class HomeTheaterFacade:
    def __init__(self, projector: Projector, sound_system: SoundSystem, streaming_service: StreamingService):
        self.projector = projector
        self.sound_system = sound_system
        self.streaming_service = streaming_service

    def start_movie(self, title: str) -> None:
        print("Starting home theater...")
        self.projector.on()
        self.sound_system.on()
        self.sound_system.set_volume(10)
        self.streaming_service.connect()
        self.streaming_service.play_movie(title)
        print("Movie has started!")

    def end_movie(self) -> None:
        print("Shutting down home theater...")
        self.streaming_service.disconnect()
        self.sound_system.off()
        self.projector.off()
        print("Home theater is off.")

projector = Projector()
sound_system = SoundSystem()
streaming_serivce = StreamingService()

home_theater = HomeTheaterFacade(projector, sound_system, streaming_serivce)
home_theater.start_movie("Inception")
home_theater.end_movie()