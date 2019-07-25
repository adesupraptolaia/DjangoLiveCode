from django import forms
from .models import *

class InputBarang(forms.ModelForm):
    class Meta:
        model = barang
        fields = ('nama', 'harga',  'foto', 'deskripsi')
    