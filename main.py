from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont


image = Image.open("images/image1.png")

draw = ImageDraw.Draw(image)


font = ImageFont.truetype("fonts/ArianaVioleta-dz2K.ttf", 200)

fill_color = (203,201,201)

watermark_text = "Playmoprojects"



draw.text((250, 400), watermark_text, font = font, fill=fill_color) 
image.show()
