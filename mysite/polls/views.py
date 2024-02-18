from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def front_page(request):
    return render(request, 'front_page.html')