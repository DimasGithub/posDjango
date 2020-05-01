from django.shortcuts import render, redirect
from .table import FormPembelian, FormJualan
from django.db.models import Max, Min, F
from .models import barang, barangJualan
def KelontongIndex(request):
    barangs = barang.objects.all()
    
    context={
        'title':'TOKO KELONTONG',
        'head':'SELAMAT DATANG',
        'table': barangs,
    }
    return render(request, 'kelontong/index.html', context)
def KelontongPembelian(request):
    tableForm = FormPembelian(request.POST or None)
    if request.method == "POST":
        if tableForm.is_valid():
            tableForm.save()
            return redirect('kelontong:KelontongIndex')
        
    context={
        'title':'PEMBELIAN',
        'table': tableForm,
    }
    return render(request, 'kelontong/pembelian.html', context)
def KelontongPenjualan(request):
    Formjualan = FormJualan(request.POST or None)
    if request.method == "POST":
          if Formjualan.is_valid():
              nama_barang = Formjualan.cleaned_data['nama_barang']
              print(nama_barang)
              Formjualan.save()
              return redirect('kelontong:KelontongPenjualan')        
    context={
        'title':'PENJUALAN',
        'table': Formjualan,
    }
    return render(request, 'kelontong/penjualan.html', context)

def CekBarang(request, namabarang):
    if barang.objects.filter(nama_barang__iexact = namabarang ).exists():
        a = "on"
        print(a)
        print('data ada')
        return redirect('kelontong:KelontongPenjualan')
    else:
        a = "off"
        print(a)
        print('data kosong')
        return redirect('kelontong:KelontongPenjualan')
    return render(request, 'kelontong/penjualan.html', context)