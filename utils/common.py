import requests


def send_whatsapp_message(user_id: str,
                          text: str,
                          ACCESS_TOKEN: str,
                          PHONE_NUMBER_ID: str):

    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": user_id,
        "type": "text",
        "text": {"body": text}
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("❌ Failed to send message:")
        print(response.text)
    else:
        print("✅ Message sent successfully")
    print("Message send status:", response.status_code, response.text)





def download_image(media_id, ACCESS_TOKEN):
    # Step 1: Get media metadata
    url = f"https://graph.facebook.com/v18.0/{media_id}"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to get media info:", response.text)
        return None

    data = response.json()
    media_url = data.get("url")

    if not media_url:
        print("No media URL found:", data)
        return None

    # Step 2: Download actual image
    image_response = requests.get(media_url, headers=headers)

    if image_response.status_code != 200:
        print("Failed to download image:", image_response.text)
        return None

    print("✅ Image downloaded successfully")
    return image_response.content  