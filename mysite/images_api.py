import requests
from random import choice
response = requests.get("https://picsum.photos/v2/list")
response.raise_for_status()

data = response.json()


all_images = [data[image]["url"] for image in range(0,30)]

random_image = choice(all_images)

print(random_image)