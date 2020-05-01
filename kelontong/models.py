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
    tgl_beli = models.DateField(auto_now_add=True, null=True, blank=True)
    tgl_kdlws = models.DateField()
    status = models.CharField(choices=status, max_length=10)
    def __str__(self):

        return "{} {}".format(self.id, self.nama_barang)
class barangJualan(models.Model):
    tanggal_jual = models.DateField(auto_now_add=True,blank=True)
    nama_barang = models.CharField(max_length=10)
    banyak_beli = models.IntegerField()
    def __str__(self):
    
        return "{} {}".format(self.id, self.nama_barang)