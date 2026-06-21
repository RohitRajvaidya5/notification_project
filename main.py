from notifier import send_notification_with_ntfy, DEFAULT_TOPIC


if __name__ == "__main__":

    send_notification_with_ntfy(
    topic=DEFAULT_TOPIC,
    title="Test Notification Alert",
    message="This is the test notification just for the demo.",
    tags=["computer"],
    priority=5
)