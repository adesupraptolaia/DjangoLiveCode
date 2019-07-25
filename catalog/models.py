from django.db import models

# Create your models here.
class barang(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255, default="a")
    test = models.SlugField(default="")

    def __str__(self):
        return self.nama