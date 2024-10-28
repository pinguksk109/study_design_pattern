class JPPlug:
    def provide_power(self) -> None:
        print("Power provided by JP plug")

class EUOutlet:
    def supply_power(self) -> None:
        print("Power supplied by EU outlet")

class PlugAdapter(JPPlug):
    def __init__(self, outlet: EUOutlet):
        self.outlet = outlet

    def provide_power(self) -> None:
        print("Using adapter to convert JP plug to EU outlet")
        self.outlet.supply_power()

def client_code(jp_plug: JPPlug) -> None:
    jp_plug.provide_power()

european_outlet = EUOutlet() 
adapter = PlugAdapter(european_outlet)

client_code(adapter)