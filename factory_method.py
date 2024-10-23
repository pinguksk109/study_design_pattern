class Notification:
    def send(self, message: str) -> None:
        pass

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"メール通知: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"SMS通知: {message}")

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unknown notification type")

def client_code(notification_type: str) -> None:
    factory = NotificationFactory()
    notification = factory.create_notification(notification_type)
    notification.send("Factory Methodの例")

client_code("email")

client_code("sms")