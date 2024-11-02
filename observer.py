class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        pass


class ConcreteObserverA(Observer):
    def update(self, message):
        print(f"Observer A received: {message}")


class ConcreteObserverB(Observer):
    def update(self, message):
        print(f"Observer B received: {message}")


subject = Subject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.add_observer(observer_a)
subject.add_observer(observer_b)

subject.notify_observers("State has changed!")