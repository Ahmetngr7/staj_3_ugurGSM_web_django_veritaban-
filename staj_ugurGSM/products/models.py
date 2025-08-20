from django.db import models


class Kategori(models.Model):
    ad = models.CharField(max_length=100)

    def __str__(self):
        return self.ad

class Urun(models.Model):
    ad = models.CharField(max_length=200)
    aciklama = models.TextField()
    fiyat = models.DecimalField(max_digits=8, decimal_places=2)
    stok = models.PositiveIntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='urunler/', blank=True, null=True)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad
