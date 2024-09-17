from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'stok', 'kategori', 'ukuran', 'warna', 'diskon', 'tanggal_dibuat')
    search_fields = ('nama', 'kategori', 'ukuran', 'warna')
