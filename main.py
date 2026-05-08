import time
from notifier import send_notification

# Drink water remainder every hour
if __name__ == "__main__":
    while True:

        send_notification("Drink Water 💧", "Hydration check!")
        
        # Wait for an hour (3600 seconds)
        time.sleep(3600)