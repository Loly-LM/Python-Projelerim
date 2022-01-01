import requests
from PIL import Image
from io import BytesIO

print("Lütfen QR koduyla eşleştirmek istediğiniz siteyi giriniz")

qrsitesi = "https://api.qrserver.com/v1/create-qr-code/"


url = "https://" + input()



resim = f"?data={url}&amp;size=500x500"
renk = "&color=556B2F"

response = requests.get(sqsitesi + resim + renk)

img = Image.open(BytesIO(response.content))

img.save("qr.png")
