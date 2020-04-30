from .models import barang
from django import forms

class FormPembelian(forms.ModelForm):
    class Meta:
        model = barang
        fields = ('nama_barang','harga_jual','harga_beli','banyak_barang','status')
        widgets = {
            'nama_barang': forms.TextInput(attrs={'class':'form-control', 'placeholder':'nama barang'}),
            'harga_beli':forms.TextInput(attrs={'class':'form-control', 'placeholder':'harga beli'}),
            'harga_jual':forms.TextInput(attrs={'class':'form-control','placeholder':'harga jual'}),
            'banyak_barang': forms.TextInput(attrs={'class':'form-control','placeholder':'banyak barang'}),
            'jenis_barang':forms.Select(attrs={'class':'form-control', 'placeholder':'PILIH'}),
            'status':forms.Select(attrs={'class':'form-control', 'placeholder':'PILIH'}),
        }
        labels ={
            'nama_barang':'NAMA BARANG',
            'harga_jual':'HARGA_JUAL',
            'harga_beli':'HARGA_BELI',
            'banyak_barang':'BANYAK BARANG',
            'jenis_barang':'JENIS BARANG',
            'status':'STATUS',
        }