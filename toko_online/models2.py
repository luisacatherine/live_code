from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.db.models import IntegerField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.utils import timezone

# Create your models here.

class Blogpost(models.Model):
    judul = models.CharField(max_length=100)
    content = models.TextField()
    foto = models.ImageField(upload_to="blog")
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.judul