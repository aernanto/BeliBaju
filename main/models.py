from django.db import models

class Product(models.Model):
    nama = models.CharField(max_length=270)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
    stok = models.PositiveIntegerField(default=0)
    kategori = models.CharField(max_length=100, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar_produk/', blank=True, null=True)
    ukuran = models.CharField(max_length=20, blank=True, null=True)  # Fitur tambahan untuk ukuran pakaian
    warna = models.CharField(max_length=50, blank=True, null=True)  # Fitur tambahan untuk warna pakaian
    diskon = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)  # Diskon sederhana, persen
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_diperbarui = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    @property
    def available(self): # kalau stoknya masih ada
        return self.stok > 0

    @property
    def harga_formatted(self):
        return f"Rp{self.harga:,.2f}"

    @property
    def harga_setelah_diskon(self):
        if self.diskon > 0:
            harga_diskon = self.harga - (self.harga * self.diskon / 100)
            return f"Rp{harga_diskon:,.2f}"
        return self.harga_terformat

    @property
    def ada_diskon(self):
        return self.diskon > 0

    class Meta:
        ordering = ['-tanggal_dibuat']
        verbose_name_plural = 'Products'