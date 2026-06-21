<p align="center">
  <img
    src="https://i.postimg.cc/52F507VM/Chat-GPT-Image-Jun-21-2026-11-10-51-PM.png"
    alt="Notification Project Banner"
    width="70%"
    style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.15);"
  >
</p>

<h1 align="center">🔔 Notification Project</h1>

<p align="center">
A lightweight Python notification service supporting Pushbullet and ntfy.sh
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/ntfy-Supported-success" alt="ntfy">
  <img src="https://img.shields.io/badge/Pushbullet-Supported-green" alt="Pushbullet">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT">
</p>

---

## 🚀 Overview

A Python-based notification framework that supports multiple notification providers with a simple and reusable API.

### Supported Providers

* Pushbullet
* ntfy.sh

### Use Cases

* Job alerts
* Hydration reminders
* Monitoring scripts
* AI agent notifications
* Scheduled reminders
* System alerts
* Automation workflows

---

## ✨ Features

### ntfy.sh Integration

* Custom notification topics
* Notification titles
* Priority levels (1–5)
* Tags / emojis
* Click actions
* Action buttons
* Custom icons
* Markdown support
* Email forwarding
* File attachments

### Pushbullet Integration

* Mobile push notifications
* Retry mechanism
* Error handling
* Logging support

### General Features

* Console and file logging
* Type hints
* Request timeout handling
* Reusable HTTP sessions (`requests.Session`)
* Environment variable support
* Modular provider architecture

---

## 📁 Project Structure

```text
NotificationProject/
│
├── notifier.py
├── main.py
├── app.log
├── .env
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository-url>
cd NotificationProject
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
PUSHBULLET_TOKEN=your_pushbullet_access_token
```

> Pushbullet credentials are only required when using Pushbullet notifications.

---

## 📢 ntfy Notification Example

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

## 📱 Pushbullet Notification Example

```python
from notifier import send_notification_with_pushnotification

send_notification_with_pushnotification(
    title="Drink Water",
    message="Hydration check!"
)
```

---

## 💧 Hydration Reminder Example

```python
import time
from notifier import send_notification_with_ntfy

while True:

    send_notification_with_ntfy(
        title="Drink Water",
        message="Hydration check!"
    )

    time.sleep(3600)
```

---

## 📝 Logging

Logs are written to:

```text
app.log
```

Example:

```text
2026-06-21 09:15:01 - INFO - Notification sent successfully (status=200)
```

---

## 📋 Notification Parameters

| Parameter | Description                             |
| --------- | --------------------------------------- |
| topic     | ntfy topic name                         |
| title     | Notification title                      |
| message   | Notification body                       |
| priority  | Notification priority (1–5)             |
| tags      | Notification emoji tags                 |
| click     | URL opened when notification is clicked |
| actions   | Interactive action buttons              |
| icon      | Custom icon URL                         |
| markdown  | Enable Markdown formatting              |
| email     | Forward notification to email           |
| attach    | Attach file URL                         |

---

## 🛠 Technologies Used

* Python
* requests
* python-dotenv
* Pushbullet API
* ntfy.sh API

---

## 🎯 Future Improvements

* Telegram integration
* Slack integration
* Discord integration
* Email notifications
* Provider abstraction layer
* Docker support
* Configuration management
* Unit tests
* CI/CD pipeline

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
