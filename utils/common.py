import requests

def send_whatsapp_message(user_id:str, text:str,ACCESS_TOKEN:str,PHONE_NUMBER_ID:str ):
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
    print("Message send status:", response.status_code, response.text)



def download_image(media_id,ACCESS_TOKEN):
    url = f"https://graph.facebook.com/v18.0/{media_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    media_url = data.get("url")
    if not media_url:
        print("No media URL found:", data)
        return
    
    image_response = requests.get(media_url, headers=headers)
    with open("received_image.jpg", "wb") as f:
        f.write(image_response.content)
    
    print("Image saved successfully!")