Nama: Aimee C. F. P. Ernanto

NPM: 2306165963

Kelas: PBP C

Link PWS: http://aimee-callista-ecommercebelibaju2.pbp.cs.ui.ac.id/

E-Commerce: Clothing

Nama e-commerce: BeliBaju


# Tugas 2


## Langkah Pengerjaan
----------------------------
### **Langkah Pertama**
- Pertama-tama, saya telah membuat direktori baru di github dan direktori lokal.
- Saya mengisi berkas README.md sebelum saya update dengan informasi yang dibutuhkan.
- Saya menginisialisasi Git pada command prompt, ```git init```.
- Dengan bantuan Chat GPT (karena saya tidak tahu cara membuat .gitignore dalam satu line di command prompt), saya kemudian menambahkan berkas .gitignore agar git tidak mengacak-acak (bukan SIAK NG..) file dan direktori yang berisi:
```
echo "# Django\n*.log\n*.pot\n*.pyc\n__pycache__\ndb.sqlite3\nmedia\n\n# Backup files\n*.bak\n\n# If you are using PyCharm\n# User-specific stuff\n.idea/**/workspace.xml\n.idea/**/tasks.xml\n.idea/**/usage.statistics.xml\n.idea/**/dictionaries\n.idea/**/shelf\n\n# AWS User-specific\n.idea/**/aws.xml\n\n# Generated files\n.idea/**/contentModel.xml\n.DS_Store\n\n# Sensitive or high-churn files\n.idea/**/dataSources/\n.idea/**/dataSources.ids\n.idea/**/dataSources.local.xml\n.idea/**/sqlDataSources.xml\n.idea/**/dynamic.xml\n.idea/**/uiDesigner.xml\n.idea/**/dbnavigator.xml\n\n# Gradle\n.idea/**/gradle.xml\n.idea/**/libraries\n\n# File-based project format\n*.iws\n\n# IntelliJ\nout/\n\n# JIRA plugin\natlassian-ide-plugin.xml\n\n# Python\n*.py[cod]\n*$py.class\n\n# Distribution / packaging\n.Python build/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\n*.egg-info/\n.installed.cfg\n*.egg\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.coverage\n.coverage.*\n.cache\n.pytest_cache/\nnosetests.xml\ncoverage.xml\n*.cover\n.hypothesis/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# pyenv\n.python-version\n\n# celery\ncelerybeat-schedule.*\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n\n# Sublime Text\n*.tmlanguage.cache\n*.tmPreferences.cache\n*.stTheme.cache\n*.sublime-workspace\n*.sublime-project\n\n# sftp configuration file\nsftp-config.json\n\n# Package control specific files Package\nControl.last-run\nControl.ca-list\nControl.ca-bundle\nControl.system-ca-bundle\nGitHub.sublime-settings" > .gitignore
```
- Saya kemudian melakukan ```git add .``` dan ```git commit -m "Tugas 2 First Commit```.
- Tak lupa, saya menghubungkan repositori lokal dengan GitHub saya dengan melakukan ```git remote add origin https://github.com/aernanto/Tugas2PBP.git```.
- Sebagai penutup langkah pertama, saya tak lupa untuk melakukan push, ```git push -u origin main```.


### **Langkah Kedua**
- Tak lupa, saya menjalankan virtual environment dengan melakukan ```python -m venv env``` lalu mengaktivasinya dengan ```env\Scripts\activate``` pada command prompt.
- Saya lalu membuat berkas requirements.txt yang berisikan:
```
django
pillow
django-crispy-forms
django-allauth
```
- Setelah requirements.txt telah dibuat, saya menjalankan ```pip install -r requirements.txt```.
- Untuk membuat proyek Django BeliBaju, saya kemudian membuka command prompt dan menjalankan ```django-admin startproject ecommerce_belibaju```.
- Karena saya telah membuat direktori proyek Django, dengan saya telah berada di direktori yang tepat, saya membuat app bernama main dengan cara ```python manage.py startapp main```.
- Saya menambahkan main ke dalam INSTALLED_APPS pada settings.py sebagai berikut:
```
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
...
```
- Saya membuat direktori baru bernama templates dalam app main. Kemudian, saya membuat berkas baru bernama main.html yang berisikan:
```
<h1>BeliBaju</h1>

<h5>NPM: </h5>
<p>2306165963</p> 
<h5>Name: </h5>
<p>Aimee Ernanto</p> 
<h5>Class: </h5>
<p>PBP C</p>
<h5>E-Commerce: </h5>
<p>Clothing</p> 
<h5>Nama e-commerce: </h5>
<p>BeliBaju</p> 
```
- Sesuai permintaan soal, saya membuat model pada app main dengan nama Product sebagai berikut:
```   
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
```
- Berikutnya, saya melakukan migrasi dengan menjalankan ```python manage.py makemigrations``` lalu diikuti dengan ```python manage.py migrate```
- Sebagai template HTML, views.py saya berisi:
```
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165963',
        'name': 'Aimee Ernanto',
        'class': 'PBP C',
        'ecommerce': 'Clothing',
        'nama_ecommerce': 'BeliBaju',
    }

    return render(request, "main.html", context) 
```
- Dalam rangka routing, saya membuat file urls.py di folder yang masih sama, yaitu main, dengan kode sebagai berikut:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
- Setelah itu, saya meng-update urls.py saya di direktori proyek Django dengan kode sebagai berikut:
```
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

### **Langkah Ketiga**
- Saya memodifikasi template main.html agar mengikuti struktur kode Django sebagai berikut:
```
<h1>BeliBaju</h1>

<h5>NPM: </h5>
<p>{{ npm }}<p>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
<h5>E-Commerce: </h5>
<p>{{ ecommerce }}</p> 
<h5>Nama e-commerce: </h5>
<p>{{ nama_ecommerce }}</p> 
```
- Proyek Django saya jalankan dengan command ```python manage.py runserver``` dan saya buka di http://localhost:8000/ .
- Untuk memodifikasi sedikit berkas tests.py pada direktori app main, saya dibantu Chat GPT (karena sedikit lupa konsep Python) agar menjadi seperti berikut ini:
```
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
```
- Lagi dan lagi, tes akan dijalankan dengan cara ```python manage.py test```
- Terakhir, saya menjalankan:
```
git add .
git commit -m "<pesan_commit>" (berkali-kali saya lakukan)
git push -u origin main
```


### **Langkah Ketiga**
Deployment PWS saya lakukan akhir-akhir karena saya lupa.
- Mengikuti langkah-langkah seperti Tutorial 0, saya login ke akun PWS saya.
- Proyek baru saya dibuat dengan nama ecommercebelibaju.
- Lalu, saya mengubah ALLOWED_HOSTS pada settings.py sehingga menjadi seperti ini:
```
...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "aimee-callista-ecommercebelibaju.pbp.cs.ui.ac.id"]
...
```
- Saya melakukan kembali:
```
git add, commit seperti awal
git branch -M main
git push pws main:master
```


## Request Client
![IMG_0633](https://github.com/user-attachments/assets/a2690d3f-67bf-4653-8663-2abbf0c2c7b5)
Pertama-tama, sebelum diteruskan ke server Django, user atau client mengakses URL melalui browser. Django kemudian akan memeriksa urls.py untuk mencocokkan pola URL dengan permintaan tersebut. Jika cocok, permintaan diteruskan ke views.py yang mengandung logika bisnis dari sebuah app. Data dari database bisa diambil melalui model yang ada di models.py, yang mengelola dan mengambil data dari database, misalnya dalam hal BeliBaju, data produk diambil dari katalog.

Setelah data diambil oleh views.py, Django akan menggunakan template HTML untuk me-render data agar bisa ditampilkan ke client. Hasil render tersebut dikirim sebagai respons HTTP ke browser user, di mana halaman yang sudah diproses akan ditampilkan. 


## useran Git
Git sendiri merupakan tool dalam Software Development untuk membantu tim bekerja sama secara efisien. Dalam Git, developer dapat menyimpan, mengatur, dan berbagi perubahan kode secara mudah karena memungkinkan developer untuk membuat branch sendiri dalam pengerjaan suatu fitur atau perbaikan, lalu menggabungkannya kembali ke proyek utama setelah selesai, tanpa mengganggu pekerjaan orang lain. 

Tak hanya itu, Git dapat medukung kerja sama secara lebih seamless karena terdapat fitur seperti fork, clone, merge, dan pull request yang memudahkan kontribusi dan integrasi dari banyak orang. Selain itu, Git juga mendukung adanya rollback jika terjadi kesalahan, sehingga tim dapat dengan cepat memperbaiki masalah tanpa kehilangan data penting. 


## useran Django
Django, seperti yang telah diketahui, mendukung pembuatan aplikasi web yang kuat dan efisien. Django memungkinkan pembuatan platform interaktif antara perusahaan dan user, seperti yang terlihat pada contoh situs e-commerce, blog pribadi, dan portal berita. Dengan Django, perusahaan dapat menjangkau audiens secara efektif melalui situs web yang user-friendly. 

Selain itu, Django sangat cocok untuk pemula karena dokumentasinya yang lengkap dan terstruktur dengan baik, sehingga sangat memudahkan proses pembelajaran. Django juga berintegrasi secara erat dengan Python, bahasa pemrograman yang telah dipelajari pada mata kuliah DDP-1, sehingga saya sebagai pemula bisa me-review kembali konsep Python yang sudah "berdebu". Dengan banyaknya library dan fitur bawaan, seperti autentikasi user dan manajemen database, Django memungkinkan developer untuk fokus pada logika aplikasi tanpa harus memikirkan hal-hal teknis yang rumit.


## ORM pada Django
Object-Relational Mapper (ORM) pada Django merupakan salah satu pilar utama Django yang menyediakan abstraksi untuk bekerja dengan basis data, dengan cara yang sebagian besar tidak bergantung pada jenis basis data tertentu. Dengan menggunakan ORM, developer dapat memodelkan tabel dalam basis data menggunakan kelas Python, yang memungkinkan interaksi data tanpa menulis query SQL secara langsung.

ORM mempermudah pengelolaan data dengan mengubah instruksi Python menjadi query SQL yang sesuai. Hal tersebut dapat mengurangi kebutuhan untuk menulis kode SQL manual, meminimalkan risiko kesalahan, dan meningkatkan produktivitas pengembangan. 


# Tugas 3


## Langkah Pengerjaan
----------------------------
### **Langkah Pertama**
- Pertama-tama, saya membuat file HTML baru bernama `base.html` pada direktori templates yang berisi:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- Pada `settings.py` saya kemudian menambahkan hal di bawah ini pada variabel TEMPLATES:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- Lalu di `main.html` pada subdirektori `templates`, saya menambahkan:
```
{% extends 'base.html' %}
{% block content %}
<h1>{{ nama_ecommerce }}</h1>

<h5>NPM: </h5>
<p>{{ npm }}<p>

<h5>Name: </h5>
<p>{{ name }}<p>

<h5>Class: </h5>
<p>{{ class }}<p>

<h5>E-Commerce: </h5>
<p>{{ ecommerce }}</p>

<h5>Nama e-commerce: </h5>
<p>{{ nama_ecommerce }}</p>

{% endblock content %}
```

### **Langkah Kedua**
- Pada file `models.py`, saya kemudian menambahkan `import uuid` sehingga menjadi seperti ini:
```
import uuid
from django.db import models

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
```
- Menutup langkah kedua, saya kemudian melakukan `python manage.py makemigrations` dan `python manage.py migrate`

### **Langkah Ketiga**
- Setelah menambahkan `forms.py` pada direktori `main`, kode saya menjadi seperti:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['nama', 'harga', 'deskripsi', 'stok', 'kategori', 'gambar', 'ukuran', 'warna', 'diskon']
```
Hal tersebut merujuk pada requirements yang saya inginkan untuk BeliBaju.
- Pada file `views.py`, saya tak lupa make sure bahwa import akan menjadi seperti:
```
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
```
- Pada file `views.py` juga, saya tak lupa untuk menambahkan function baru bernama `tambah_produk` yang nantinya menerima parameter `request` karena nantinya data akan secara otomatis ter-update jikalau ada submission. Dengan bantuan Chat GPT, saya menambahan kode:
```
def tambah_produk(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle data POST dan FILES untuk gambar
        if form.is_valid():
            form.save()  # Save data product baru ke database
            return redirect('daftar_produk')  # Redirect ke page daftar produk 
    else:
        form = ProductForm()  # Buat form kosong kalau bukan POST

    return render(request, 'tambah-produk.html', {'form': form})  # Render form di template
```
- Lalu saya akan mengubah function `show_main` menjadi seperti:
```
def show_main(request):
    products = Product.objects.all()  # Akses semua product dari database

    context = {
        'name': 'Aimee Ernanto',  
        'class': 'PBP C',
        'npm': '2306165963',
        'ecommerce': 'Clothing',  
        'nama_ecommerce': 'BeliBaju',  
        'products': products  
    }

    return render(request, "main.html", context)  # Render main page dengan context
```
- Pada `urls.py`, saya kemudian melakukan dua hal:
1) Import function yang telah saya buat sebelumnya,
```
from django.urls import path
from . import views
from main.views import tambah_produk, show_main
```
2) Menambahkan path pada variabel `urlpatterns` pada `urls.py`,
```
urlpatterns = [
    path('', views.show_main, name='show_main'), 
    path('tambah-produk/', views.tambah_produk, name='tambah_produk'),
]
```
- Lalu saya buat file html baru bernama `tambah-produk.html` yang berisi:
```
{% extends 'base.html' %} 
{% block content %}
<h1>Tambah Produk Baru</h1>

<form method="POST" enctype="multipart/form-data"> 
  {% csrf_token %}
  <table>
    {{ form.as_table }}  
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Tambah Produk" />  
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
- Benchmarking dari Tutorial 2, saya kemudian melengkapi file `main.html` saya, sehingga menjadi:
```
{% extends 'base.html' %}
{% block content %}
<h1>{{ nama_ecommerce }}</h1>

<h5>NPM: </h5>
<p>{{ npm }}<p>

<h5>Name: </h5>
<p>{{ name }}<p>

<h5>Class: </h5>
<p>{{ class }}<p>

<h5>E-Commerce: </h5>
<p>{{ ecommerce }}</p>

<h5>Nama e-commerce: </h5>
<p>{{ nama_ecommerce }}</p>

<h2>Daftar Produk</h2>

{% if not products %}
<p>Belum ada produk yang tersedia di {{ nama_ecommerce }}.</p>
{% else %}
<table>
  <tr>
    <th>Nama Produk</th>
    <th>Harga</th>
    <th>Stok</th>
    <th>Diskon</th>
  </tr>

  {% for product in products %}
  <tr>
    <td>{{ product.nama }}</td>
    <td>{{ product.harga_formatted }}</td>
    <td>{{ product.stok }}</td>
    <td>
      {% if product.ada_diskon %}
        {{ product.diskon }}%
      {% else %}
        Tidak ada diskon
      {% endif %}
    </td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:tambah_produk' %}">
  <button>Tambah Produk Baru</button>
</a>
{% endblock content %}
```
- Tak lupa saya menjalankan `python manage.py runserver` dan membuka http://localhost:8000/ untuk melihat hasil sementara.

### **Langkah Keempat**
- Saya menambahkan beberapa import pada `views.py` agar menjadi:
```
from django.http import HttpResponse, JsonResponse
from django.core import serializers
```
- Dengan bantuan Chat GPT, saya menambahkan beberapa function baru, yaitu `show_xml` dan `show_json` yang menerima parameter request sehingga kode akan menjadi seperti:
```
def show_xml(request):
    data = Product.objects.all()  # Mengambil semua data dari model Product
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")  

def show_json(request):
    products = Product.objects.all()
    data = list(products.values('id', 'nama', 'harga', 'deskripsi', 'stok', 'kategori', 'ukuran', 'warna', 'diskon', 'tanggal_dibuat', 'tanggal_diperbarui'))
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})  
```
- Lalu, tak lupa saya meng-import function yang telah saya buat sebelumnya pada `urls.py`:
```
from main.views import tambah_produk, show_main, show_xml, show_json
```
- Terakhir, saya akan menambahkan beberapa path url dalam variabel `urlpatterns` yang akan menjadi seperti ini:
```
urlpatterns = [
    path('', views.show_main, name='show_main'), 
    path('tambah-produk/', views.tambah_produk, name='tambah_produk'),  
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```
- Tak lupa saya menjalankan `python manage.py runserver` dan membuka http://localhost:8000/xml/ dan http://localhost:8000/json/ untuk melihat hasil sementara. Saya tak lupa mencatat ID yang muncul.

### **Langkah Keempat**
- Dengan bantuan Chat GPT, pada `views.py`, saya membuat function-function baru yang lagi-lagi menerima request dan ID dengan nama `show_xml_by_id` dan `show_json_by_id` seperti di bawah ini:
1) `show_xml_by_id`
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)  # Mengambil data Product berdasarkan id
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
2) `show_json_by_id`
```
def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id).first()  # Mengambil data Product berdasarkan id
    if product:
        data = {
            'id': str(product.id),
            'nama': product.nama,
            'harga': str(product.harga),
            'deskripsi': product.deskripsi,
            'stok': product.stok,
            'kategori': product.kategori,
            'ukuran': product.ukuran,
            'warna': product.warna,
            'diskon': str(product.diskon),
            'tanggal_dibuat': product.tanggal_dibuat.isoformat(),
            'tanggal_diperbarui': product.tanggal_diperbarui.isoformat()
        }
        return JsonResponse(data, json_dumps_params={'indent': 2})  # Added indent for readability
    else:
        return JsonResponse({'error': 'Product not found'}, status=404)
```
- Pada `urls.py`, saya akan melengkapi import sehingga menjadi seperti:
```
from main.views import tambah_produk, show_main, show_xml, show_json, show_xml_by_id, show_json_by_id
```
- Tak lupa juga, saya menambahkan path URL ke dalam variabel `urlpatterns` sehingga lengkapnya akan menjadi seperti:
```
urlpatterns = [
    path('', views.show_main, name='show_main'), 
    path('tambah-produk/', views.tambah_produk, name='tambah_produk'),  
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
]
```
- Tak lupa saya menjalankan `python manage.py runserver` dan membuka `http://localhost:8000/xml/[id]/` atau `http://localhost:8000/json/[id]/` untuk melihat hasil sementara dengan ID yang telah disimpan.

### **Langkah Kelima**
- Setelah men-screenshot hasil yang muncul pada Postman, saya melakukan push ke PWS dengan membuat subdirektori `.github` yang memiliki subdirektori lagi bernama `workflows`. Lalu saya membuat file `deploy.yml` yang berisi:
```
name: Push to PWS

on:
  push:
    branches: [ main ]
    paths-ignore:
        - '**.md'
  pull_request:
    branches: [ main ]
    paths-ignore:
        - '**.md'

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2
      with:
        fetch-depth: 0

    - name: Set up Git
      run: |
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'

    - name: Check PWS remote, pull, merge, and push
      env:
        PWS_URL: ${{ secrets.PWS_URL }}
      run: |
          # Check if master branch exists locally
          if ! git show-ref --verify --quiet refs/heads/master; then
            echo "Creating master branch"
            git branch master
          fi
          
          # Switch to master branch
          git checkout master

          # Push to master branch and capture the output
          push_output=$(git push $PWS_URL main:master 2>&1)
          if [[ $? -ne 0 ]]; then
            echo "Push failed with output: $push_output"
            echo "Error: Unable to push changes. Please check the error message above and resolve any conflicts manually."
            exit 1
          fi
          echo "Push successful with output: $push_output"
```
- Saya kemudian mengisi New repository secret, merujuk pada Tutorial 2.
- Pada `settings.py`, saya kemudian menambahkan:
```
CSRF_TRUSTED_ORIGINS = ["http://localhost","http://127.0.0.1","http://aimee-callista-ecommercebelibaju.pbp.cs.ui.ac.id/", "http://aimee-callista-ecommercebelibaju.pbp.cs.ui.ac.id/"]
```
- Setelah melakukan git add, commit, push, proyek pada PWS saya telah successfully built.


## Data delivery dalam implementasi platform
Data delivery merupakan bagian penting dalam implementasi platform data karena arsitekturnya yang mendukung berbagai aspek penting, seperti tujuan bisnis, sumber data, kualitas data, tata kelola data, dan keamanan data. Tetapi, dalam best practicenya, banyak organisasi dan perusahaan yang terjebak dalam pengembangan sistem data yang terisolasi. Misalnya, mereka memiliki data warehouse untuk reporting secara tradisional, data lake berbasis Hadoop untuk analisis mendalam, sistem transfer file lama, gateway API untuk aplikasi mobile, serta aplikasi streaming berbasis Kafka. Hal tersebut disebabkan oleh sistem-sistem yang sering kali tidak saling terintegrasi, tidak memiliki teknologi atau spesifikasi yang sama, dan dikelola oleh kelompok pengembang yang berbeda. Pendekatan terisolasi tersebut mengakibatkan berbagai masalah, seperti penurunan waktu yang dibutuhkan untuk menghasilkan laporan dan analisis, ketidak konsistenan laporan, duplikasi data, serta biaya pengembangan yang lebih tinggi. Maka dari itu, data delivery lebih unggul dalam menyatukan berbagai sistem menjadi lebih transparan dan efisien dalam data-based decision making.


## Efektivitas XML dan JSON, serta keunggulan JSON
JSON dan XML merupakan format data yang sering digunakan untuk pertukaran informasi antar sistem, namun JSON lebih populer dibandingkan XML karena beberapa alasan mendasar. JSON, subset dari JavaScript, memiliki struktur yang lebih sederhana dan langsung dibandingkan XML, sehingga JSON lebih mudah diproses dan digunakan langsung dalam JavaScript tanpa perlu melakukan parsing tambahan. JSON juga menghindari useran tag yang panjang dan berlebihan seperti pada XML, sehingga ukuran data yang dikirimkan lebih kecil dan lebih efisien. Hal tersebut pun mengurangi overhead dalam transmisi data dan mempermudah pengelolaan memori dan CPU pada server.

Di sisi lain, XML memiliki aturan yang lebih ketat mengenai struktur dan format, seperti kepekaan huruf besar-kecil dan larangan useran spasi dalam tag, yang dapat membuat pengolahan dan validasi XML lebih rumit. Selain itu, XML sering kali menghasilkan ukuran file yang lebih besar karena tag-tag deskriptif yang banyak. Karena format JSON lebih ringkas, JSON lebih cepat dan efisien dalam hal pertukaran data.


## Fungsi dari method `is_valid()` pada form Django
Method `is_valid()` pada form Django berfungsi untuk memvalidasi data yang dikirimkan melalui form sebelum lanjut ke steps berikutnya, seperti menyimpan data ke database. Ketika method dipanggil, Django secara otomatis memeriksa apakah data yang dimasukkan memenuhi semua aturan validasi yang telah ditentukan dalam form, seperti jenis field atau format yang benar. Jika data valid, method akan mengembalikan `True`, menandakan bahwa data dapat diproses lebih lanjut tanpa kesalahan. Sebaliknya, jika ada kesalahan atau ketidakcocokan dalam data, `is_valid()` akan mengembalikan `False`, dan form akan menampilkan error handling message yang sesuai.

Method `is_valid()` diperlukan untuk memastikan bahwa data yang diterima dari input benar-benar sesuai dengan kriteria yang diharapkan sebelum menyimpannya ke dalam sistem. 

Contoh pada kode saya:
```
def tambah_produk(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle data POST dan FILES untuk gambar
        if form.is_valid():
            form.save()  # Save data product baru ke database
            return redirect('daftar_produk')  # Redirect ke page daftar produk 
    else:
        form = ProductForm()  # Buat form kosong kalau bukan POST

    return render(request, 'tambah-produk.html', {'form': form})  # Render form di template
```

Dalam contoh kode saya di atas, jika form yang diterima dalam request POST valid, maka data produk baru akan disimpan ke database dan user akan dialihkan ke halaman daftar produk. Jika form tidak valid, data tidak akan disimpan, dan form dengan error handling message akan ditampilkan kembali.


## useran `csrf_token` pada form di Django
`csrf_token` merupakan mekanisme keamanan dalam Django untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF), jenis cyberattack di mana situs web jahat dapat memaksa browser user untuk melakukan aksi yang tidak diinginkan di situs web yang tepercaya tanpa sepengetahuan user. Misalnya, jika user telah login ke situs web perbankan secara tidak sengaja mengunjungi situs web jahat, situs jahat tersebut bisa mengirimkan request untuk melakukan transfer dana tanpa izin. `csrf_token` mencegah hal tersebut terjadi dengan memastikan bahwa setiap request POST yang dikirim ke server termasuk token CSRF yang valid. Token ini hanya dapat diterbitkan oleh server dan hanya berlaku untuk sesi user tertentu, sehingga mencegah third-party yang tidak sah untuk memanipulasi request.

Jika `csrf_token` tidak ditambahkan ke form di Django, aplikasi web akan rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan kelemahan tersebut dengan membuat formulir yang tampaknya sah di situs mereka sendiri, yang saat dikirim dapat melakukan tindakan berbahaya di situs web target yang tidak dilindungi. Dengan mengaktifkan `csrf_token` dalam setiap form, Django memastikan bahwa hanya permintaan yang berasal dari sumber yang sah dan terpercaya yang dapat memodifikasi data atau melakukan aksi sensitif pada server.


## Screenshot pengaksesan keempat URL dengan Postman:
![Screenshot (1035)](https://github.com/user-attachments/assets/75841a93-c1bf-44f3-8da7-038c1adc51f1)
![Screenshot (1034)](https://github.com/user-attachments/assets/f22fcfac-79d3-4dd9-8876-d2452e94f367)
![Screenshot (1033)](https://github.com/user-attachments/assets/1c60e11a-7732-4464-bdf2-ffd0ad76bd81)
![Screenshot (1032)](https://github.com/user-attachments/assets/936ee3e4-4bd9-47cd-8d38-329bf5ccd767)
Dapat disimpulkan bahwa URL telah menghasilkan output yang diharapkan.


# Tugas 3


## Langkah Pengerjaan
----------------------------
### **Langkah Pertama**
- Saya menambahkan `UserCreationForm` dan `messages` pada views.py:
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
- Pada views.py, saya menambahkan function register:
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Anda telah berhasil dibuat!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)
```
- Lalu, saya membuat register.html yang berisi:
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Register</h1>
  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>
{% endblock content %}
```
- Pada views.py, saya menambahkan:
```
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
```
dan juga fungsi login_user:
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
- Kemudian saya membuat login.html yang berisi:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>
  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} 
  Belum punya akun?
  <a href="{% url 'main:register' %}">Daftar Sekarang</a>
</div>
{% endblock content %}
```
- Untuk fungsi logout, saya menambahkan:
`from django.contrib.auth import logout`
dan menambahkan fungsi:
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
- Pada main.html, saya menambahkan button logout:
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
- Pada urls.py, saya meng-update seluruh informasi yang diperlukan agar menjadi:
```
from django.urls import path
from . import views
from main.views import tambah_produk, show_main, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'), 
    path('tambah-produk/', views.tambah_produk, name='tambah_produk'),  
    path('daftar-produk/', views.daftar_produk, name='daftar_produk'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```
- Saya lalu menambahkan login_required pada views.py:
```
from django.contrib.auth.decorators import login_required
```
dan decorator
```
@login_required(login_url='/login')
def show_main(request):
```
- Setelah melakukan `python manage.py runserver`, saya kemudian menambahkan import data dari cookies:
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
- Saya menambahkan cookie last_login pada login_user:
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
- Saya kemudian mengubah fungsi show_main untuk menambahkan last_login untuk menampilkan data last login
- untuk menghubungkan model dengan user, saya menambahkan field sehingga menjadi:
```
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name="user") 

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
```
- Terakhir, saya melakukan `python manage.py makemigrations` dan `python manage.py migrate`

## Perbedaan antara HttpResponseRedirect() dan redirect()
- HttpResponseRedirect() secara eksplisit me-return kode status HTTP 302 untuk mengarahkan user ke URL yang baru.
- Sedangkan redirect() lebih ringkas dan me-return objek respons pengalihan, serta dapat menerima berbagai jenis argumen, seperti URL, nama view, bahkan objek model.

## Penghubungan model Product dengan User
Penghubungan antara model `Product` dan `User` dalam aplikasi Django dilakukan melalui useran field `ForeignKey`. Pada model `Product`, terdapat atribut `user` yang bertindak sebagai penghubung dengan model `User`, yang berarti setiap produk yang dibuat akan terkait langsung dengan user tertentu, yang diidentifikasi oleh ID user. Saat user membuat produk baru, mereka secara otomatis ditetapkan sebagai pemilik produk tersebut melalui relasi ini. Relasi ini memungkinkan aplikasi untuk dengan mudah melacak siapa yang membuat atau memiliki produk tertentu, serta memudahkan dalam mengelola data user dan produk dalam konteks yang lebih luas. 
Pada kode saya, hubungan antara model Product dan model User diimplementasikan melalui useran ForeignKey pada atribut user. Pada model Product, field user merujuk pada model User yang ada di Django, sehingga setiap produk dapat terhubung dengan user tertentu yang membuatnya. useran `related_name='products'` pada field `ForeignKey` juga memungkinkan untuk mengakses semua produk yang dimiliki oleh user dengan lebih sederhana.

## Perbedaan antara Authentication dan Authorization
Authentication adalah proses verifikasi identitas user, memastikan bahwa user tersebut adalah siapa yang mereka klaim. Saat user login, mereka memasukkan kredensial (username dan password) yang kemudian diverifikasi oleh sistem.
Sedangkan Authorization adalah proses untuk menentukan hak akses user setelah mereka terautentikasi, memutuskan apakah user memiliki izin untuk melakukan tindakan atau mengakses resource tertentu.

### Cara Django mengingat user yang telah login
Django mengelola sesi user menggunakan cookies untuk menyimpan informasi sesi. Saat user berhasil login, Django membuat sesi baru dan menyimpannya di server. Di sisi klien, Django mengirimkan cookie yang berisi ID sesi. Cookie tersebut digunakan untuk melacak status login user di seluruh aplikasi. Lalu, cookies juga menyimpan preferensi user, riwayat pencarian, dan item keranjang belanja. 


# Tugas 2


## Langkah Pengerjaan
----------------------------
- Dalam file base.html, saya membuat kerangka dasar untuk semua halaman dalam aplikasi BeliBaju. Saya menyusun struktur HTML yang mencakup elemen-elemen seperti <head> untuk pengaturan metadata, termasuk pemanggilan stylesheet dan font dari Google Fonts. Di bagian <body>, saya mengintegrasikan navigasi yang sticky dengan menggunakan Tailwind CSS, sehingga navbar tetap terlihat saat pengguna menggulir halaman. 
- Pada file navbar.html, saya menambahkan elemen navigasi interaktif yang menyesuaikan dengan status autentikasi pengguna. Di sini, saya menyertakan tautan ke halaman produk dan form untuk menambahkan produk baru. Saya memastikan tampilan navbar responsif dengan menyertakan tombol menu mobile yang dapat memperlihatkan opsi-opsi navigasi saat perangkat berukuran kecil. JavaScript digunakan untuk mengontrol visibilitas menu mobile, sehingga meningkatkan pengalaman pengguna pada perangkat seluler.
- lalu dalam file daftar_produk.html, saya mengimplementasikan halaman yang menampilkan daftar produk yang tersedia. Saya menggunakan grid layout untuk menyusun kartu produk dengan rapi dan memastikan informasi penting seperti nama, harga, deskripsi, dan stok ditampilkan dengan jelas. Saya juga menyertakan tombol untuk mengedit dan menghapus produk, yang terhubung langsung dengan fungsi yang sesuai di backend. Saya menambahkan elemen navigasi kembali ke halaman sebelumnya menggunakan tombol panah, sehingga pengguna dapat dengan mudah kembali tanpa kesulitan.
- Saya menambahkan beberapa view di Django untuk menambah, mengedit, dan menghapus produk. Di sini, saya berfokus pada pembuatan antarmuka yang intuitif dan responsif. Saya juga menyusun URL yang relevan untuk setiap fungsi, memastikan bahwa semua tautan di navbar dan halaman produk saling terhubung dengan benar. Ini termasuk penggunaan metode GET dan POST untuk mengelola interaksi pengguna dengan produk, serta menerapkan autentikasi untuk mengamankan akses ke fungsi tertentu.
- Lalu saya menggunakan Tailwind CSS untuk styling, yang memungkinkan saya mengatur tampilan dan nuansa aplikasi dengan cepat.


### Urutan Prioritas CSS Selector
Dalam CSS, urutan prioritas untuk pengambilan selector ditentukan oleh beberapa aturan. Pertama, ada aturan spesifisitas, di mana selector dengan spesifisitas yang lebih tinggi akan diutamakan. Spesifisitas dihitung berdasarkan jenis selector: ID (1), class (0.1), dan elemen (0.01). Jika beberapa selector diterapkan pada elemen yang sama, maka selector ID akan memiliki prioritas tertinggi, diikuti oleh selector class, dan terakhir selector elemen. Misalnya, jika ada satu selector ID, satu selector class, dan satu selector elemen yang diterapkan pada elemen yang sama, maka yang akan digunakan adalah style dari selector ID. Lalu, ada aturan cascading yang berarti bahwa jika dua aturan memiliki spesifisitas yang sama, aturan yang ditulis terakhir dalam file CSS akan diterapkan. 

### Pentingnya Responsive Design
Responsive design merupakan pendekatan penting dalam pengembangan aplikasi web karena memungkinkan tampilan konten yang optimal di berbagai device, mulai dari desktop hingga smartphone. Dengan meng-adjust tata letak, ukuran gambar, dan elemen lainnya sesuai dengan ukuran layar, user tidak perlu melakukan zoom in atau out. Lalu hal ini juga membantu dalam SEO, karena search engine lebih suka situs yang mobile-friendly.

### Perbedaan Margin, Border, dan Padding
Margin, border, dan padding merupakan tiga konsep penting dalam CSS yang berfungsi mengatur ruang di sekitar elemen HTML. Margin merupakan ruang luar yang mengelilingi elemen, memisahkan elemen tersebut dari elemen lain di sekitarnya. Border merupakan garis yang mengelilingi elemen, dan dapat memiliki warna, ketebalan, dan gaya yang berbeda. Padding merupakan ruang di dalam elemen antara konten dan border yang memberikan jarak antara isi elemen dengan batasnya.
Untuk mengimplementasikan ketiga hal tersebut dalam CSS, developer dapat menggunakan properti `margin`, `border`, dan `padding`. Misalnya, untuk menambahkan margin, Anda bisa menggunakan `margin: 20px;` untuk memberikan ruang luar sebesar 20 piksel. Border dapat ditambahkan dengan `border: 1px solid black;` untuk memberikan garis hitam dengan ketebalan 1 piksel. Sedangkan padding bisa ditentukan dengan `padding: 15px;` untuk memberi ruang 15 piksel di dalam elemen. Kombinasi penggunaan ketiga properti ini akan menghasilkan tata letak yang lebih teratur dan estetis.

### Konsep Flexbox dan Grid Layout
Flexbox dan Grid Layout merupakan dua sistem layout CSS yang kuat untuk membantu merancang tata letak web yang responsif dan dinamis. Flexbox, atau Flexible Box Layout, dirancang untuk mengatur elemen dalam satu dimensi (baik secara horizontal maupun vertikal). Dengan menggunakan properti seperti `display: flex;`, elemen dapat dengan mudah diatur untuk mengisi ruang yang tersedia, dengan kemampuan untuk mengubah ukuran dan posisi secara dinamis berdasarkan ukuran layar. Flexbox sangat cocok untuk membuat menu navigasi atau komponen yang memerlukan pengaturan dalam satu baris atau kolom.

Di sisi lain, Grid Layout dirancang untuk mengatur elemen dalam dua dimensi (baris dan kolom). Dengan menggunakan `display: grid;`, developer dapat membuat grid dengan berbagai ukuran dan memposisikan elemen di dalamnya secara lebih kompleks. Grid sangat berguna untuk layout yang lebih rumit, seperti galeri gambar atau tata letak halaman yang memerlukan pembagian yang lebih terstruktur. Keduanya memberikan fleksibilitas dan kontrol yang lebih besar dalam mengatur elemen di halaman web, dan keduanya sering digunakan bersamaan untuk menciptakan desain yang responsif dan menarik.


# Tugas 6


## Langkah Pengerjaan
----------------------------
### **Langkah Pertama**
- Pertama-tama, saya menambahkan Error Message Pada Login saya, sehingga akan menjadi seperti:
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))  # Set cookie last_login
            return response
    else:
        form = AuthenticationForm()  # Membuat form AuthenticationForm baru untuk request GET
        messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'login.html', {'form': form})
```
- Kemudian saya memmbuat Fungsi untuk Menambahkan Mood dengan AJAX
```
@csrf_exempt
@require_POST
def tambah_produk_ajax(request):
    nama = request.POST.get("nama")
    harga = request.POST.get("harga")
    deskripsi = request.POST.get("deskripsi")
    stok = request.POST.get("stok")
    kategori = request.POST.get("kategori")
    ukuran = request.POST.get("ukuran")
    warna = request.POST.get("warna")
    diskon = request.POST.get("diskon")
    user = request.user

    produk_baru = Product(
        nama=nama,
        harga=harga,
        deskripsi=deskripsi,
        stok=stok,
        kategori=kategori,
        ukuran=ukuran,
        warna=warna,
        diskon=diskon,
        user=user
    )
    produk_baru.save()

    return HttpResponse(b"CREATED", status=201)
```
- JavaScript memiliki peran penting dalam pengembangan aplikasi web karena memungkinkan interaksi dinamis dan responsif. Dengan JavaScript, pengembang dapat memperbarui konten halaman secara real-time tanpa perlu melakukan reload seluruh halaman, yang sangat meningkatkan pengalaman pengguna. Selain itu, kemampuan untuk mengelola elemen DOM langsung di sisi client memudahkan proses manipulasi konten secara cepat dan efisien. Dalam konteks framework modern seperti React atau Vue.js, JavaScript juga memberikan struktur yang baik untuk mengembangkan aplikasi dengan antarmuka yang kompleks dan modular.
- Fungsi await dalam fetch() sangat penting karena memastikan JavaScript menunggu respons dari server sebelum melanjutkan eksekusi kode berikutnya. Dengan menggunakan await, kita bisa menghindari situasi di mana data dari server belum siap tetapi sudah diproses oleh kode yang seharusnya menunggu hasil tersebut. Tanpa await, proses fetch() berjalan secara asinkron, sehingga kode setelahnya bisa dijalankan lebih dulu, yang bisa mengakibatkan error atau data yang ditampilkan tidak lengkap. Sebagai contoh, jika kita melakukan fetch data produk dari server dan tidak menggunakan await, data yang ditampilkan mungkin belum tersedia dan hasilnya akan salah atau tidak ada sama sekali.
- Decorator csrf_exempt diperlukan pada view yang menggunakan AJAX POST karena Django secara default melindungi setiap permintaan POST dengan CSRF token untuk mencegah serangan Cross-Site Request Forgery. Jika token CSRF tidak dikirimkan dalam permintaan AJAX POST, maka Django akan menolak permintaan tersebut. Penggunaan csrf_exempt memungkinkan kita untuk menonaktifkan pengecekan token CSRF pada view tertentu sehingga permintaan AJAX POST dapat tetap diproses. Namun, penggunaan decorator ini harus dilakukan dengan hati-hati, hanya pada permintaan yang benar-benar aman, karena menonaktifkan CSRF bisa membuka celah keamanan jika tidak diterapkan dengan benar.
- Validasi data di backend sangat penting meskipun validasi di frontend juga dilakukan. Alasan utamanya adalah keamanan dan integritas data. Validasi di frontend memang bisa memberikan umpan balik yang cepat kepada pengguna, tetapi data yang dikirim melalui frontend dapat dimanipulasi menggunakan alat seperti developer tools. Oleh karena itu, validasi di backend berfungsi sebagai lapisan perlindungan terakhir untuk memastikan data yang diterima server sudah benar dan aman. Backend juga memastikan bahwa semua data yang masuk melalui API atau form mengikuti aturan yang ditetapkan tanpa bergantung pada bagaimana data tersebut dikirim.
- Untuk implementasi checklist secara step-by-step, saya memulainya dengan menyiapkan view dan template di Django yang akan menampilkan data dari database. Setelah itu, saya menambahkan fungsionalitas AJAX menggunakan JavaScript dengan fetch() yang menangani permintaan GET dan POST. await saya gunakan untuk memastikan respons dari server sudah siap sebelum memperbarui tampilan di halaman. Selanjutnya, saya menambahkan modal form yang dirancang menggunakan Tailwind CSS untuk pengiriman data baru melalui AJAX POST. Di backend, saya menerapkan validasi untuk memastikan data yang dikirim melalui form tersebut sudah sesuai. Setelah data berhasil divalidasi, saya memastikan bahwa halaman diperbarui secara dinamis menggunakan JavaScript tanpa perlu melakukan reload penuh, sehingga interaksi pengguna tetap lancar dan cepat.
