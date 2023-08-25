from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):

    urunler = Urun.objects.all()
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(isim__icontains=search)

    context = {
        'urunlerim': urunler,
        'search': search
    }

    return render(request, 'index.html', context)

def olustur(request):
        if request.method == "POST":
            resim = request.FILES["foto"]
            isim = request.POST["isim"]
            aciklama = request.POST["aciklama"]
            fiyat = request.POST["fiyat"]

            urun = Urun.objects.create(
                isim = isim,
                resim = resim,
                aciklama = aciklama,
                fiyat = fiyat
            )
            urun.save()
            return redirect("index")
        return render(request, 'olustur.html')

