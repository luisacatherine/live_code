from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.db.models import IntegerField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.utils import timezone

# Create your models here.

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="product")
    harga = models.CharField(max_length=50)
    update_at = models.DateTimeField(auto_now=True)
    deskripsi_produk = models.TextField()
    def __str__(self):
        return self.nama