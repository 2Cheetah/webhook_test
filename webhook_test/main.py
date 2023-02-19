import requests
import os

chatforma_api_key = os.getenv('CHATFORMA_API_KEY')

url_check_auth = "https://api.pro.chatforma.com/public/v1/auth-test"
url_get_bots = "https://api.pro.chatforma.com/public/v1/bots"
url_get_forms = "https://api.pro.chatforma.com/public/v1/forms"
url_get_notification_sample = "https://api.pro.chatforma.com/public/v1/notification-sample"


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



if __name__ == "__main__":
    api_key = os.getenv("CHATFORMA_API_KEY")
    bots = Bots(api_key)
    bots.get_data()
    
    forms = Forms(api_key, '124442')
    forms.get_data()
    
    notification_sample = NotificationSample(api_key, '124442', 'iqepgkqtlm')
    notification_sample.get_data()

    notification = Notifications(api_key, '124442')
#    notification.subscribe('iqepgkqtlm', 'https://gunicorn-test.onrender.com/test')

#    notification.unsubscribe("37263")
    
    notification.get_notifications_list("iqepgkqtlm")
