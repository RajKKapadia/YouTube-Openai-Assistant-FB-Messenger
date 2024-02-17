import requests

import config


def send_message_to_fb_messenger(recipient_id: str, message_text: str) -> None:
    url = f"https://graph.facebook.com/v17.0/me/messages?access_token={config.FB_PAGE_ACCESS_TOKEN}"
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message. Status code:", response.status_code)
