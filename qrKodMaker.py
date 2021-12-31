import requests
from PIL import Image
from io import BytesIO

print("Lütfen QR koduyla eşleştirmek istediğiniz siteyi giriniz")

endpoint = "https://api.qrserver.com/v1/create-qr-code/"


url = "https://" + input()



orn = f"?data={url}&amp;size=500x500"
color = "&color=556B2F"

response = requests.get(endpoint + orn + color)

img = Image.open(BytesIO(response.content))

img.save("qr.png")
