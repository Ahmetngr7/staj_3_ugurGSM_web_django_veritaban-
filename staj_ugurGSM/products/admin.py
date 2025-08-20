# products/admin.py
from django.contrib import admin
from .models import Urun, Kategori

admin.site.register(Urun)
admin.site.register(Kategori)
