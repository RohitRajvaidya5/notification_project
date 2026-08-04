from notifier import send_notification_with_ntfy, DEFAULT_TOPIC
from datetime import datetime
import time


def send_every_hour_notification():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_notification_with_ntfy(
            topic="hourly-tracker",
            title="Hourly Notification",
            message=f"Current time: {current_time} : Let's keep track of the time and stay productive!",
            tags=["hourly"],
            priority=4
        )
        time.sleep(3600)


if __name__ == "__main__":
    send_every_hour_notification()
