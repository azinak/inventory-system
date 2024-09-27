from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')



def products(request):
    return render(request, "products/index.html")