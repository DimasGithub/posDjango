from django.db import models
class barang(models.Model):
    nama_barang = models.CharField(max_length=10)
    harga_beli = models.IntegerField()
    harga_jual = models.IntegerField()
    banyak_barang = models.IntegerField()
    jenisbarang = (
        ('OBAT-OBATAN','obat-obatan'),
        ('MAKANAN DAN MINUMAN RINGAN ','makananminuman'),
    )
    jenis_barang = models.CharField(choices=jenisbarang, max_length=30, default='lain-lain')
    status = (
        ('ADA', 'ADA'),
        ('KOSONG', 'KOSONG'),
    )
    status = models.CharField(choices=status, max_length=10)

    def __str__(self):

        return "{} {}".format(self.id, self.nama_barang)
