import requests

url = "http://127.0.0.1:8000/predict"

files = {
    "file": open("TomatoYellowCurlVirus2.JPG", "rb")   # field name MUST be "file"
}

response = requests.post(url, files=files)

print(response.json())