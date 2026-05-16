from notifier import send_notification
from datetime import datetime

current_hour = datetime.now().hour

# Send notifications only between 7 AM and 11 PM
if 7 <= current_hour < 23:
    send_notification("Drink Water 💧", "Hydration check!")
    print("Notification sent!")
else:
    print("Quiet hours. No notification sent.")