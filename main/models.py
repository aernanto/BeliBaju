import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=270, verbose_name="Nama Produk")
    harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Harga")
    deskripsi = models.TextField(verbose_name="Deskripsi")
    stok = models.PositiveIntegerField(default=0, verbose_name="Stok")
    kategori = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kategori")
    gambar = models.ImageField(upload_to='gambar_produk/', blank=True, null=True, verbose_name="Gambar")
    ukuran = models.CharField(max_length=20, blank=True, null=True, verbose_name="Ukuran")  # Fitur tambahan untuk ukuran pakaian
    warna = models.CharField(max_length=50, blank=True, null=True, verbose_name="Warna")  # Fitur tambahan untuk warna pakaian
    diskon = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, verbose_name="Diskon")  # Diskon sederhana, persen
    tanggal_dibuat = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Dibuat")
    tanggal_diperbarui = models.DateTimeField(auto_now=True, verbose_name="Tanggal Diperbarui")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name="Pengguna") 

    def __str__(self):
        return self.nama

    @property
    def available(self):  # kalau stoknya masih ada
        return self.stok > 0

    @property
    def harga_formatted(self):
        return f"Rp{self.harga:,.2f}"

    @property
    def harga_setelah_diskon(self):
        if self.diskon > 0:
            harga_diskon = self.harga - (self.harga * self.diskon / 100)
            return f"Rp{harga_diskon:,.2f}"
        return self.harga_formatted

    @property
    def ada_diskon(self):
        return self.diskon > 0

    class Meta:
        ordering = ['-tanggal_dibuat']
        verbose_name_plural = 'Products'