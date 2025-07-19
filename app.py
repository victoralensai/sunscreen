import schedule
import time
import threading
from src.notification import NotificationNtfy

class MainApp:
    def __init__(self, location: str, ntfy_topic_prefix: str, time_to_send: str = "08:00"):
        self.location = location
        self.ntfy_topic_prefix = ntfy_topic_prefix
        self.ntfy = NotificationNtfy(location, ntfy_topic_prefix)
        self.time_to_send = time_to_send

    def send_daily_sunscreen_reminder(self):
        """Send the daily sunscreen notification"""
        print(f"Sending daily sunscreen reminder at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        self.ntfy.sunscreen_today_notification()

    def run_scheduler(self):
        """Run the scheduler in a separate thread"""
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

    def run(self):
        # Schedule notifications at specific times
        schedule.every().day.at(self.time_to_send).do(self.send_daily_sunscreen_reminder)

        # Start scheduler in background thread
        scheduler_thread = threading.Thread(target=self.run_scheduler, daemon=True)
        scheduler_thread.start()
        
        print("Sunscreen reminder app started!")
        print(f"Scheduled notifications: {self.time_to_send} on topic {self.ntfy_topic_prefix} for location {self.location}, url will be {self.ntfy.get_notification_url()}")

        # Keep the main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("App stopped!")

if __name__ == "__main__":

    # ===== CHANGE CONFIGURATION HERE =====
    # Set your location and ntfy topic prefix
    # You can also set the time you want the notification to be sent
    # Default is 08:00 (8 AM)
    LOCATION = "Brest, Bretagne" # Be sure to write the location like this: 'City, Region, Country'
    NTFY_TOPIC_PREFIX = "jOEp52eCQOXGUYTo" # Replace with your ntfy topic prefix, I recommend you to use a random string
    TIME_TO_SEND = "07:00"  # Time to send the notification, in HH:MM format
    # ======================================
    
    app = MainApp(LOCATION, NTFY_TOPIC_PREFIX, TIME_TO_SEND)
    app.run()