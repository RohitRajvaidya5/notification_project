# Notification Project

A Python-based notification service supporting multiple notification providers.

Currently supported providers:

* Pushbullet
* ntfy.sh

The project can be used for:

* Job alerts
* Hydration reminders
* Monitoring scripts
* AI agent notifications
* Scheduled reminders
* System alerts

---

## Features

### ntfy Support

* Custom notification topics
* Notification titles
* Priority levels (1-5)
* Tags / emojis
* Click actions
* Action buttons
* Custom icons
* Markdown support
* Email forwarding
* File attachments

### Pushbullet Support

* Push notifications to mobile devices
* Retry mechanism
* Error handling
* Logging support

### General Features

* Logging to console and file
* Type hints
* Request timeout handling
* Connection reuse using `requests.Session`
* Modular notification provider design

---

## Project Structure

```text
NotificationProject/
│
├── notifier.py
├── main.py
├── app.log
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd NotificationProject
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
PUSHBULLET_TOKEN=your_pushbullet_access_token
```

The Pushbullet token is only required when using Pushbullet notifications.

---

## ntfy Example

```python
from notifier import send_notification_with_ntfy

send_notification_with_ntfy(
    topic="job-alerts",
    title="Backend Engineer Role",
    message="New Python Backend Engineer role found.",
    priority=5,
    tags=["briefcase", "rocket"],
    click="https://example.com/job",
    actions=[
        "view,Open Job,https://example.com/job"
    ]
)
```

---

## Pushbullet Example

```python
from notifier import send_notification_with_pushnotification

send_notification_with_pushnotification(
    title="Drink Water",
    message="Hydration check!"
)
```

---

## Hydration Reminder Example

```python
import time

while True:

    send_notification_with_ntfy(
        title="Drink Water",
        message="Hydration check!"
    )

    time.sleep(3600)
```

---

## Logging

Logs are written to:

```text
app.log
```

Example:

```text
2026-06-21 09:15:01 - INFO - Notification sent successfully (status=200)
```

---

## Notification Parameters

| Parameter | Description                          |
| --------- | ------------------------------------ |
| topic     | ntfy topic name                      |
| title     | Notification title                   |
| message   | Notification body                    |
| priority  | 1-5 notification priority            |
| tags      | Notification emoji tags              |
| click     | URL opened when notification clicked |
| actions   | Notification action buttons          |
| icon      | Custom icon URL                      |
| markdown  | Enable markdown formatting           |
| email     | Forward notification to email        |
| attach    | Attach file URL                      |

---

## Future Improvements

* Telegram integration
* Slack integration
* Discord integration
* Email notifications
* Notification provider abstraction layer
* Docker support
* Configuration management
* Unit tests

---

## Technologies Used

* Python
* requests
* python-dotenv
* ntfy.sh
* Pushbullet

---

## License

MIT License
