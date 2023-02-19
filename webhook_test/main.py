import requests
import os


class Bots:
    def __init__(self, api_key):
        self.url = "https://api.pro.chatforma.com/public/v1/bots"
        self.headers = {
            "accept": "application/json",
            "api_key": api_key,
        }


    def get_data(self):
        result = requests.get(self.url, headers=self.headers)
        print(result.json())


class Forms(Bots):
    def __init__(self, api_key, botId):
        self.url = f"https://api.pro.chatforma.com/public/v1/forms?botId={botId}"
        self.headers = {
            "accept": "application/json",
            "api_key": api_key,
        }


class NotificationSample(Forms):
    def __init__(self, api_key, botId, formId):
        self.url = f"https://api.pro.chatforma.com/public/v1/notification-sample?botId={botId}&formId={formId}"
        self.headers = {
            "accept": "application/json",
            "api_key": api_key,
        }


class Notifications(Forms):
    def __init__(self, api_key, botId):
        self.botId = botId
        self.headers = {
            "accept": "application/json",
            "api_key": api_key,
        }

    def subscribe(self, formId, target_url):
        url = "https://api.pro.chatforma.com/public/v1/subscribe-notification"
        subscribe_data = {
            "botId": self.botId,
            "formId": formId,
            "target_url": target_url,
        }
        response = requests.post(
            url,
            headers=self.headers,
            data=subscribe_data
        )
        print(response)
        print(response.json())

    def unsubscribe(self, subscriptionId):
        url = "https://api.pro.chatforma.com/public/v1/unsubscribe-notification"
        unsubscribe_data = {
            "botId": self.botId,
            "subscriptionId": subscriptionId,
        }

        response = requests.delete(
            url,
            headers = self.headers,
            data=unsubscribe_data,
        )

        print(response)
#        print(response.json())
    
    def get_notifications_list(self, formId):
        url = f"https://api.pro.chatforma.com/public/v1/notification?botId={self.botId}&formId={formId}"
        response = requests.get(url, headers=self.headers)
        print(response)
        print(response.json())


class Message(Forms):
    def __init__(self, api_key, botId):
        self.botId = botId
        self.url = f"https://api.pro.chatforma.com/public/v1/bots/{self.botId}/messages"
        self.headers = {
            "accept": "application/json",
            "api_key": api_key,
        }

    def send_message(self, userId, message):
        url = f"https://api.pro.chatforma.com/public/v1/bots/{self.botId}/dialogs/{userId}/message"
        message_data = {
            "uid": userId,
            "message": message,
        }
        
        response = requests.post(
            url,
            headers=self.headers,
            data=message_data,
        )

        print(response)
        # print(response.json)


class User(Forms):
    def __init__(self, api_key, botId):
        self.url = f"https://api.pro.chatforma.com/public/v1/bots/{botId}/users"
        self.headers = {
            "accept": "application/json",
            "api_key": api_key,
        }


if __name__ == "__main__":
    api_key = os.getenv("CHATFORMA_API_KEY")

#     print("Fetching list of Bots...")
#     bots = Bots(api_key)
#     bots.get_data()
    
#     print("\nFetching list of Forms...")
#     forms = Forms(api_key, '124442')
#     forms.get_data()
    
#     print("\nNotification sample:")
#     notification_sample = NotificationSample(api_key, '124442', 'iqepgkqtlm')
#     notification_sample.get_data()

    print("\nFetching list of notification subscriptions:")
    notification = Notifications(api_key, '124442')
#    notification.subscribe('iqepgkqtlm', 'https://gunicorn-test.onrender.com/test')

    print("Unsubscribing from notifications...")
    notification.unsubscribe(37265)
    
    notification.get_notifications_list("iqepgkqtlm")

    # print("\nFetching list of messages from bot...")
    # messages = Message(api_key, '124442')
    # messages.get_data()

    # print("\nFetching list of Bot users...")
    # user = User(api_key, botId='124442')
    # user.get_data()

    # message = "Test message to a user"
    # print("\nSending message...")
    # messages.send_message(userId=51884226, message=message)