
response = requests.get("https://picsum.photos/200")
response.raise_for_status()

image_content = response.content  # Use content for non-JSON responses

# Now you can save the image, display it, or perform other actions with the binary content
with open("image.jpg", "wb") as f:
    f.write(image_content)

print("Image downloaded successfully")