from django.shortcuts import render, redirect
from add_watermark import add_watermark_to_image
from images_api import get_random_image
from .all_forms import SignUp
from django.contrib.auth.hashers import make_password
from .models import Users


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
    if request.method == "POST":
        sign_up = SignUp(request.POST)
        if sign_up.is_valid():
            username = sign_up.cleaned_data["username"]
            password = sign_up.cleaned_data["password"]

            hashed_password = make_password(password)

            user = Users(username=username, password=hashed_password)
            user.save()

            return redirect('front_page')
        
        return redirect(request, 'front_page')
    return render(request, 'sign_up.html', {'form': SignUp()})
        