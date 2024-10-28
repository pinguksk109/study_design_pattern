class USB:
    def connect_with_use_cable(self) -> None:
        raise NotImplementedError("You shold implements this method!")
    
class MicroUSB:
    def connect_with_microusb_cable(self) -> None:
        print("Connected with MicroUSB cable")

class MicroUSBToUSBAdapter(USB):
    def __init__(self, micro_usb_device: MicroUSB):
        self.micro_usb_device = micro_usb_device
    
    def connect_with_use_cable(self) -> None:
        self.micro_usb_device.connect_with_microusb_cable()

def client_code(usb_device: USB) -> None:
    usb_device.connect_with_use_cable()

micro_usb_device = MicroUSB()
usb_adapter = MicroUSBToUSBAdapter(micro_usb_device)

client_code(usb_adapter)