from dotenv import load_dotenv
import requests
import os
import time
import logging
from typing import Optional, List
import requests


DEFAULT_TOPIC = "test-ntfy-notification"

# Reusable HTTP client
session = requests.Session()

load_dotenv()

ACCESS_TOKEN = os.getenv("PUSHBULLET_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError(
        "PUSHBULLET_TOKEN not found in environment variables"
    )

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


def send_notification_with_pushnotification(
    title: str,
    message: str,
    retries: int = 3,
    delay: int = 2
):
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

    for attempt in range(retries):

        try:
            response = requests.post(
                url,
                json=data,
                headers=headers,
                timeout=10
            )

            if response.status_code == 200:
                logging.info(
                    "Notification sent successfully"
                )
                return True

            logging.error(
                f"Pushbullet error: {response.text}"
            )

        except requests.exceptions.RequestException as e:
            logging.error(str(e))

        time.sleep(delay)

    logging.error(
        "Failed to send notification after retries"
    )

    return False


def send_notification_with_ntfy(
    topic: str = DEFAULT_TOPIC,          # Channel/topic name
    message: str = "Default Message",    # Notification body
    title: Optional[str] = None,         # Notification title
    priority: int = 3,                   # 1=min, 2=low, 3=default, 4=high, 5=max
    tags: Optional[List[str]] = None,    # ["rocket", "warning"]
    click: Optional[str] = None,         # URL opened when notification clicked
    markdown: bool = False,              # Enable markdown rendering
    attach: Optional[str] = None,        # File URL attachment
    icon: Optional[str] = None,          # Icon URL
    email: Optional[str] = None,         # Forward notification to email
    actions: Optional[List[str]] = None  # Action buttons
) -> requests.Response | None:
    """
    Send a notification using ntfy.sh.

    Args:
        topic: ntfy topic name.
        message: Notification body.
        title: Notification title.
        priority: Integer from 1-5.

    Returns:
        requests.Response on success, None on failure.
    """

    try:
        headers = {}

        if title:
            headers["Title"] = title

        if not 1 <= priority <= 5:
            raise ValueError("priority must be between 1 and 5")

        headers["Priority"] = str(priority)

        if tags:
            headers["Tags"] = ",".join(tags)

        if click:
            headers["Click"] = click

        if markdown:
            headers["Markdown"] = "yes"

        if attach:
            headers["Attach"] = attach

        if icon:
            headers["Icon"] = icon

        if email:
            headers["Email"] = email

        if actions:
            headers["Actions"] = ";".join(actions)

        response = session.post(
            f"https://ntfy.sh/{topic}",
            data=message.encode("utf-8"),
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        logging.info(
            f"Notification sent successfully "
            f"(status={response.status_code})"
        )

        return response

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send notification: {e}")
        return None