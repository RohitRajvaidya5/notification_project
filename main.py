import time
from notifier import send_notification
from datetime import datetime



# Drink water remainder every hour
if __name__ == "__main__":
    while True:

        # current_hour = datetime.now().hour


        # if 0 <= current_hour < 7:
        #     # Sleep until 7 AM
        #     hours_until_7am = (7 - current_hour) % 24
        #     time.sleep(hours_until_7am * 3600)
        #     print("It's 7 AM! Time to start your hydration routine.")
        
        # else:

        #     send_notification("Drink Water 💧", "Hydration check!")
        #     time.sleep(3600)
        send_notification("Drink Water 💧", "Hydration check!")

