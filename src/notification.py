import requests
import re

class NotificationNtfy:
    def __init__(self, location: str, ntfy_topic_prefix: str, ntfy_url: str = "https://ntfy.sh", uv_api_url: str = "https://f1.vctor.me"):
        self.location = location
        self.ntfy_topic_prefix = ntfy_topic_prefix
        self.ntfy_url = ntfy_url
        self.uv_api_url = uv_api_url

    def test_notification(self):
        print(f"Testing notification for {self.location} on topic {self.ntfy_topic_prefix}")
        topic_url = self.get_notification_url()

        headers = {
            "Title": "test notification",
            "Tags": self.location,
            "Priority": "low",
        }

        try:
            response = requests.post(topic_url, data=f"test notification with location : {self.location}", headers=headers)
            response.raise_for_status()
            return {"success": True, "message": "Notification sent successfully"}
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}
        
    def get_notification_url(self):
        """
        Returns the URL for the notification topic.
        """
        return f"{self.ntfy_url}/{self.ntfy_topic_prefix}_{re.sub(r'[^A-Za-z]', '', self.location)}"
    
    def send_notification(self, message: str, title: str, tags: str = "", priority: str = "default"):
        topic_url = self.get_notification_url()

        headers = {
            "Title": title,
            "Tags": tags,
            "Priority": priority,
        }

        try:
            response = requests.post(topic_url, data=message, headers = headers)
            response.raise_for_status()
            return {"success": True, "message": "Notification sent successfully"}
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}

    def sunscreen_today_notification(self):
        uv_hours_response = requests.get(url=f"{self.uv_api_url}/sunscreen/hours?location={self.location}")
        if uv_hours_response.status_code == 200:
            print(uv_hours_response.content)
            uv_hours = uv_hours_response.json().get("sunscreen_hours", [])
            if uv_hours:
                start_hour, end_hour = uv_hours[0]
                if start_hour != 0:
                    message = f"Today, you should put sunscreen on from hour {start_hour} to hour {end_hour} in {self.location}."
                    self.send_notification(message, "Sunscreen Reminder", tags=self.location)
                else:
                    message = f"No sunscreen needed today in {self.location}."
                    self.send_notification(message, "Sunscreen Reminder", tags=self.location)
        else:
            error_message = f"Error: {uv_hours_response.status_code} - {uv_hours_response.text}"
            self.send_notification(error_message, "Sunscreen Error", priority="high")
            raise Exception(error_message)

if __name__ == "__main__":
    # Example usage
    ntfy = NotificationNtfy(location="Los Angeles, USA", ntfy_topic_prefix="jOEp52eCQOXGUYTo")
    result = ntfy.test_notification()
    print(ntfy.get_notification_url())
    # print(result)

    # ntfy.send_notification(
    #     message="This is a test notification",
    #     title="Test Notification",
    #     tags="test,example",
    #     priority="min"
    # )

    # ntfy.sunscreen_today_notification()
