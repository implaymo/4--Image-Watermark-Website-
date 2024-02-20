from django.shortcuts import render
from add_watermark import add_watermark_to_image
from images_api import get_random_image
from forms import Login, SignUp
from django.contrib.auth.hashers import make_password
from models import Users


def front_page(request):
    image_data = get_random_image()
    image_path = image_data
    output_path = "static/image1_with_watermark.png"
    text = "Playmoprojects"
    font_path = "fonts/ArianaVioleta-dz2K.ttf"
    font_size = 200
    fill_color = (169, 169, 169, 100)

    # Apply watermark
    add_watermark_to_image(image_path, output_path, text, font_path, font_size, fill_color)

    return render(request, 'front_page.html')
    
def sign_up(request):
    if request.methods == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        hashed_password = make_password(password)
        
        user = Users(username=username, password=hashed_password)
        user.save()
        
        