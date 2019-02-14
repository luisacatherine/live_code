from django.contrib import admin
from .models import Produk

# Register your models here.
my_model = [Produk]
admin.site.register(my_model)