# Publisher（ニュース発行者）
class NewsPublisher:
    def __init__(self):
        self.subscribers = []  # 登録された購読者（Observer）のリスト

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)  # 各Subscriberに通知

# Subscriber（ニュース購読者のインターフェース）
class Subscriber:
    def update(self, news):
        pass

# 具体的なSubscriberの実装
class EmailSubscriber(Subscriber):
    def update(self, news):
        print(f"Email Subscriber received news: {news}")

class SMSSubscriber(Subscriber):
    def update(self, news):
        print(f"SMS Subscriber received news: {news}")

class PushNotificationSubscriber(Subscriber):
    def update(self, news):
        print(f"Push Notification Subscriber received news: {news}")

# 使用例
publisher = NewsPublisher()

email_subscriber = EmailSubscriber()
sms_subscriber = SMSSubscriber()
push_notification_subscriber = PushNotificationSubscriber()

# 購読者を登録
publisher.add_subscriber(email_subscriber)
publisher.add_subscriber(sms_subscriber)
publisher.add_subscriber(push_notification_subscriber)

# ニュースを配信
publisher.notify_subscribers("Breaking News: Observer Pattern Explained!")
