from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont


def add_watermark_to_image(image_path, output_path, text, font_path, font_size, fill_color):
    # Open the image
    image = Image.open(image_path)

    # Add the watermark
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((250, 400), text, font=font, fill=fill_color)

    # Save the modified image
    image.save(output_path)
