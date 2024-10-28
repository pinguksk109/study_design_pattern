class TicketType:
    def __init__(self, departure: str, destination: str, price: int):
        self.departure = departure
        self.destination = destination
        self.price = price

class TicketFactory:
    _tickets = {}

    @classmethod
    def get_ticket_type(cls, departure: str, destination: str, price: int):
        key = (departure, destination, price)
        if key not in cls._tickets:
            cls._tickets[key] = TicketType(departure, destination, price)
        return cls._tickets[key]
    
class TrainTicket:
    def __init__(self, ticket_type: TicketType, travel_date: str, seat_number: str):
        self.ticket_type = ticket_type
        self.travel_date = travel_date
        self.seat_number = seat_number

    def display_ticket_info(self):
        print(f"Departure: {self.ticket_type.departure}, "
              f"Destination: {self.ticket_type.destination}, "
              f"Price: {self.ticket_type.price}, "
              f"Date: {self.travel_date}, Seat: {self.seat_number}")
        
def issue_tickets():
    factory = TicketFactory()

    tokyo_to_osaka_ticket = factory.get_ticket_type("Tokyo", "Osaka", 14000)
    tokyo_to_kyoto_ticket = factory.get_ticket_type("Tokyo", "Kyoto", 12000)

    tickets = [
        TrainTicket(tokyo_to_osaka_ticket, "2023-10-01", "12A"),
        TrainTicket(tokyo_to_osaka_ticket, "2023-10-01", "12B"),
        TrainTicket(tokyo_to_kyoto_ticket, "2023-10-01", "14A"),
        TrainTicket(tokyo_to_kyoto_ticket, "2023-10-02", "15A")
    ]

    for ticket in tickets:
        ticket.display_ticket_info()

issue_tickets()