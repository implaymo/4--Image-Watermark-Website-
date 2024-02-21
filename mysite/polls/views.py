from django.shortcuts import render, redirect
from add_watermark import add_watermark_to_image
from images_api import get_random_image
from .all_forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm




def front_page(request):
    image_data = get_random_image()
    image_path = image_data
    output_path = "static/image1_with_watermark.png"
    text = "Playmoprojects"
    font_path = "fonts/ArianaVioleta-dz2K.ttf"
    font_size = 200
    fill_color = (169, 169, 169, 100)

    add_watermark_to_image(image_path, output_path, text, font_path, font_size, fill_color)

    return render(request, 'front_page.html')
    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('front_page')
    else:
        form = RegisterForm()

    return render(request, "sign_up.html", {'form': form})


def signin(request):
    pass

        