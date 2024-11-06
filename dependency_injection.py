class Service:
    def perform(self):
        print("Service is performing an action")

class Client:
    def __init__(self, service: Service):
        self.service = service

    def do_work(self):
        self.service.perform()

service = Service()
client = Client(service)
client.do_work()