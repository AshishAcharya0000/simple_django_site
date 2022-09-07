from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about_us.html')

def more(request):
    return render(request, 'more.html')