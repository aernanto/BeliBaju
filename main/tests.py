from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class ProductTest(TestCase):

    def setUp(self):
        """Inisialisasi data yang sering digunakan di beberapa tes"""
        self.client = Client()
        self.now = timezone.now()
        self.product = Product.objects.create(
            nama="Produk Test",
            harga=100000,
            deskripsi="Deskripsi produk test",
            stok=10,
            kategori="Kategori Test",
            ukuran="M",
            warna="Merah",
            diskon=10.00,
            tanggal_dibuat=self.now,
            tanggal_diperbarui=self.now
        )

    def test_main_url_is_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = self.client.get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_harga_setelah_diskon(self):
        """Test harga setelah diskon diterapkan"""
        expected_harga_diskon = self.product.harga - (self.product.harga * self.product.diskon / 100)
        self.assertEqual(self.product.harga_setelah_diskon, f"Rp{expected_harga_diskon:,.2f}")

    def test_ada_diskon(self):
        """Test apakah produk memiliki diskon"""
        self.assertTrue(self.product.ada_diskon)

    def test_harga_formatted(self):
        """Test format harga"""
        self.assertEqual(self.product.harga_formatted, "Rp100,000.00")