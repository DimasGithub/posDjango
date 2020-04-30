from django.urls import path
from . import views 
urlpatterns = [
    path('', views.KelontongIndex, name="KelontongIndex"),
    path('pembelian/', views.KelontongPembelian, name="KelontongPembelian"),

]
