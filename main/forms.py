from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['nama', 'harga', 'deskripsi', 'stok', 'kategori', 'gambar', 'ukuran', 'warna', 'diskon']