import requests
from io import BytesIO
from PIL import Image

res = requests.get('https://httpbin.org/image', headers={'Accept': 'image/webp'})
img_bytes = BytesIO(res.content)
img = Image.open(img_bytes)
img.save('image.webp')
payload = {'name': 'Timur', 'job': 'developer'}
res = requests.post('https://httpbin.org/post',data=payload)
print(res.text)
