from django.shortcuts import render
from .models import Urun

def urun_listesi(request):
    urunler = Urun.objects.all()
    return render(request, 'products/urun_listesi.html', {'urunler': urunler})
