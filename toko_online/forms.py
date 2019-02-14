from django import forms
from .models import Produk

class PostForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ('nama', 'foto', 'harga', 'deskripsi_produk')