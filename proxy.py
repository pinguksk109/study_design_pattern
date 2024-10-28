from abc import ABC, abstractmethod
import time

class Image(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class ReadImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_image()

    def _load_image(self) -> None:
        print(f"Loading image from {self.filename}...")
        time.sleep(2)
    
    def display(self) -> None:
        print(f"Displaying {self.filename}")

class ImageProxy(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None

    def display(self) -> None:
        if self._real_image is None:
            self._real_image = ReadImage(self.filename)
        self._real_image.display()

def main():
    image = ImageProxy("high_resolution_image.jpg")
    print("ImageProxy created.\n")

    image.display()

    image.display()

main()