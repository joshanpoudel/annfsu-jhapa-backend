from firebase_admin import messaging


def send_fcm_notifications(fcm_token, title, body):
    try:
        message = messaging.Message(
            notification=messaging.Notification(title, body), token=fcm_token
        )

        response = messaging.send(message)
        print(f"Successfully sent message: {response}")
    except Exception as e:
        print(f"Error sending message: {e}")
