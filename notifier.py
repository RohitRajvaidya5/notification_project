import requests
from dotenv import load_dotenv
import os
import time
import logging

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Replace with your Pushbullet Access Token
ACCESS_TOKEN = os.getenv("access_token")

def send_notification(title, message, retries=3, delay=2):
    url = "https://api.pushbullet.com/v2/pushes"
    
    headers = {
        "Access-Token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    
    data = {
        "type": "note",
        "title": title,
        "body": message
    }

    attempts = 0

    while attempts < retries:
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                logging.info("Notification sent successfully!")
                return
            else:
                logging.error(f"Failed to send notification: {response.text}")
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred: {e}")
        
        attempts += 1
        logging.info(f"Retrying... ({attempts}/{retries})")
        time.sleep(delay)

    logging.error("Failed to send notification after multiple attempts.")
    time.sleep(delay)

