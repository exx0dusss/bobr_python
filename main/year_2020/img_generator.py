import requests
import os
from io import BytesIO
from PIL import Image
api_key_pixabay = '20269355-cd39894102aeebbc857a8e6f4'
query = 'Lviv'
url = f'https://pixabay.com/api/?key={api_key_pixabay}&q={query}&image_type=photo'
res = requests.get(url).json()
img_obj_list = res['hits']

def save_image(img_obj):
    jpg_name = f"{img_obj['tags'].replace(',','_')}.jpg"
    print(f'Downloading picture {jpg_name}')
    img_res = requests.get(img_obj['largeImageURL'])
    jpg = Image.open(BytesIO(img_res.content))
    jpg.save(jpg_name)
    print(f'Picture {jpg_name} was successfully saved')

for el in range(5):
    img_obj = img_obj_list[el]
    save_image(img_obj)