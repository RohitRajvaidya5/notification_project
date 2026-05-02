import time
from notifier import send_notification

# Drink water remainder every hour
if __name__ == "__main__":
    while True:

        send_notification(
            "Drink Water", 
            "It's time to drink water! Stay hydrated!"
            )
        
        # Wait for an hour (3600 seconds)
        time.sleep(3600)