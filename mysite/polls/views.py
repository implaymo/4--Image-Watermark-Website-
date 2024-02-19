from django.shortcuts import render
from add_watermark import add_watermark_to_image


def front_page(request):
    image_path = "static/image1.png"
    output_path = "static/image1_with_watermark.png"
    text = "Playmoprojects"
    font_path = "fonts/ArianaVioleta-dz2K.ttf"
    font_size = 200
    fill_color = (203, 201, 201)

    # Apply watermark
    add_watermark_to_image(image_path, output_path, text, font_path, font_size, fill_color)

    return render(request, 'front_page.html')
    