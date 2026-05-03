# Replace with your Pushbullet Access Token
import os


ACCESS_TOKEN = os.getenv("PUSHBULLET_TOKEN")
print(ACCESS_TOKEN)
print("TOKEN PRESENT:", ACCESS_TOKEN is not None)