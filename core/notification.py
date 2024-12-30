from firebase_admin import messaging


def send_fcm_notification(fcm_token, title, body):
    try:
        message = messaging.Message(
            notification=messaging.Notification(title=title, body=body),
            android=messaging.AndroidConfig(
                notification=messaging.AndroidNotification(
                    body=body
                    
                )
            ),
            token=fcm_token
        )

        response = messaging.send(message)
        print(f"Successfully sent message: {response}")
    except Exception as e:
        print(f"Error sending message: {e}")

def notify_user(user, title, body):
    if user.fcm_token:
        send_fcm_notification(user.fcm_token, title, body)
    else:
        print("User does not have an FCM token.")
