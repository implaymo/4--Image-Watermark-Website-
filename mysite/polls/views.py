from django.shortcuts import render, redirect
from add_watermark import add_watermark_to_image
from images_api import get_random_image
from .all_forms import RegisterForm, SignInForm
from django.contrib.auth import authenticate, login, logout





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
            form.save()
            return redirect('front_page')
        else:
            error_message = "Something went wrong. Try again"
    else:
        error_message = "Something went wrong. Try again"
        form = RegisterForm()

    return render(request, "register.html", {'form': form, 'error_message': error_message})


def sign_in(request):
    error_message = None
    if request.method == "POST":
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            print(username)
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("front_page")
            else:
                error_message = "Wrong credentials, try again."
        else:
            error_message = "Form is not valid."
    else:
        form = SignInForm()
            
    return render(request, 'sign_in.html', {'form': form, 'error_message': error_message})


def logout_user(request):
    logout(request)
    return redirect("front_page")
            
        