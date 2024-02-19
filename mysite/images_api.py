import requests


def get_random_image():

    response = requests.get("https://picsum.photos/1000")
    response.raise_for_status()

    image_content = response.content  

    with open("static/image.jpg", "wb") as f:
        f.write(image_content)

    image_path = "static/image.jpg"
    return image_path