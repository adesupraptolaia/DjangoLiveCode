from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import Http404

# Create your views here.
def home(request):
    Barang = barang.objects.all()
    return render(request, 'home.html', {'barang' : Barang})

def barang_detail(request, barang_id):
    try:
        Barang = barang.objects.get(id = barang_id)
    except:
        raise Http404("Blog does not exist")
    return render(request, 'barang_detail.html', {'barang':Barang})

def inputbarang(request):
    if request.method == "POST":
        form = InputBarang(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = InputBarang()
    return render(request, 'inputbarang.html', {'form': form})
