from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    SEHIR_SECENEKLERI = [
        ('IST', 'İstanbul'),
        ('ANK', 'Ankara'),
        ('IZM', 'İzmir'),
        ('ANT', 'Antalya'),
        ('BUR', 'Bursa'),
        ('DİĞ', 'Diğer'),
    ]
    
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE)
    sehir = models.CharField(max_length=3, choices=SEHIR_SECENEKLERI)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    adres = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.kullanici.username
