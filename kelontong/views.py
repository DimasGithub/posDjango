from django.shortcuts import render, redirect
from .table import FormPembelian
from .models import barang
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
    if tableForm.is_valid():
        tableForm.save()
        return redirect('kelontong:KelontongIndex')
    
    context={
        'title':'PEMBELIAN',
        'table': tableForm,
    }
    return render(request, 'kelontong/pembelian.html', context)