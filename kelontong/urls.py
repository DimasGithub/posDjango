from django.urls import path
from . import views 
urlpatterns = [
    path('', views.KelontongIndex, name="KelontongIndex"),
    path('pembelian/', views.KelontongPembelian, name="KelontongPembelian"),
    path('penjualan/', views.KelontongPenjualan, name="KelontongPenjualan"),
    path('penjualan/<str:namabarang>', views.CekBarang, name="CekBarang"),

]
