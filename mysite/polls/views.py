from django.shortcuts import render, redirect
from add_watermark import add_watermark_to_image
from images_api import get_random_image
from .all_forms import SignUp, Login
from django.contrib.auth.hashers import make_password, check_password
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

def login(request):
    if request.method == "POST":
        login = Login()
        if login.is_valid():
            print("SUCCESS2")
            username = login.cleaned_data["username"]
            password = login.cleaned_data["password"]
            try:
                user = Users.objects.get(username=username)
            except Users.DoesNotExist:
                print("NOT FOUND1")
                return render(request, 'login.html', {'error_message': 'Invalid username or password'})
            
            if check_password(password, user.password):
                print("SUCCESS3")
                return redirect(request, 'front_page')
            else:
                print("NOT FOUND2")
                return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html', {'form': Login()})


            
            
        