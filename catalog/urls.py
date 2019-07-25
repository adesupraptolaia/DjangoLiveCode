from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('barang/<int:barang_id>', barang_detail, name="barang_detail"),
    path('input/', inputbarang, name="inputbarang"),
]
