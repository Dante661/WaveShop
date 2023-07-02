from django.shortcuts import render


def index(request):
    return render(request, "WaveShop/index.html")


# Create your views here.
