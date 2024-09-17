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

Setelah data diambil oleh views.py, Django akan menggunakan template HTML untuk me-render data agar bisa ditampilkan ke client. Hasil render tersebut dikirim sebagai respons HTTP ke browser pengguna, di mana halaman yang sudah diproses akan ditampilkan. 


## Penggunaan Git
Git sendiri merupakan tool dalam Software Development untuk membantu tim bekerja sama secara efisien. Dalam Git, developer dapat menyimpan, mengatur, dan berbagi perubahan kode secara mudah karena memungkinkan developer untuk membuat branch sendiri dalam pengerjaan suatu fitur atau perbaikan, lalu menggabungkannya kembali ke proyek utama setelah selesai, tanpa mengganggu pekerjaan orang lain. 

Tak hanya itu, Git dapat medukung kerja sama secara lebih seamless karena terdapat fitur seperti fork, clone, merge, dan pull request yang memudahkan kontribusi dan integrasi dari banyak orang. Selain itu, Git juga mendukung adanya rollback jika terjadi kesalahan, sehingga tim dapat dengan cepat memperbaiki masalah tanpa kehilangan data penting. 


## Penggunaan Django
Django, seperti yang telah diketahui, mendukung pembuatan aplikasi web yang kuat dan efisien. Django memungkinkan pembuatan platform interaktif antara perusahaan dan user, seperti yang terlihat pada contoh situs e-commerce, blog pribadi, dan portal berita. Dengan Django, perusahaan dapat menjangkau audiens secara efektif melalui situs web yang user-friendly. 

Selain itu, Django sangat cocok untuk pemula karena dokumentasinya yang lengkap dan terstruktur dengan baik, sehingga sangat memudahkan proses pembelajaran. Django juga berintegrasi secara erat dengan Python, bahasa pemrograman yang telah dipelajari pada mata kuliah DDP-1, sehingga saya sebagai pemula bisa me-review kembali konsep Python yang sudah "berdebu". Dengan banyaknya library dan fitur bawaan, seperti autentikasi pengguna dan manajemen database, Django memungkinkan developer untuk fokus pada logika aplikasi tanpa harus memikirkan hal-hal teknis yang rumit.


## ORM pada Django
Object-Relational Mapper (ORM) pada Django merupakan salah satu pilar utama Django yang menyediakan abstraksi untuk bekerja dengan basis data, dengan cara yang sebagian besar tidak bergantung pada jenis basis data tertentu. Dengan menggunakan ORM, developer dapat memodelkan tabel dalam basis data menggunakan kelas Python, yang memungkinkan interaksi data tanpa menulis query SQL secara langsung.

ORM mempermudah pengelolaan data dengan mengubah instruksi Python menjadi query SQL yang sesuai. Hal tersebut dapat mengurangi kebutuhan untuk menulis kode SQL manual, meminimalkan risiko kesalahan, dan meningkatkan produktivitas pengembangan. 


# Tugas 3


## Data delivery dalam implementasi platform
Data delivery merupakan bagian penting dalam implementasi platform data karena arsitekturnya yang mendukung berbagai aspek penting, seperti tujuan bisnis, sumber data, kualitas data, tata kelola data, dan keamanan data. Tetapi, dalam best practicenya, banyak organisasi dan perusahaan yang terjebak dalam pengembangan sistem data yang terisolasi. Misalnya, mereka memiliki data warehouse untuk reporting secara tradisional, data lake berbasis Hadoop untuk analisis mendalam, sistem transfer file lama, gateway API untuk aplikasi mobile, serta aplikasi streaming berbasis Kafka. Hal tersebut disebabkan oleh sistem-sistem yang sering kali tidak saling terintegrasi, tidak memiliki teknologi atau spesifikasi yang sama, dan dikelola oleh kelompok pengembang yang berbeda. Pendekatan terisolasi tersebut mengakibatkan berbagai masalah, seperti penurunan waktu yang dibutuhkan untuk menghasilkan laporan dan analisis, ketidak konsistenan laporan, duplikasi data, serta biaya pengembangan yang lebih tinggi. Maka dari itu, data delivery lebih unggul dalam menyatukan berbagai sistem menjadi lebih transparan dan efisien dalam data-based decision making.


## Efektivitas XML dan JSON, serta keunggulan JSON
JSON dan XML merupakan format data yang sering digunakan untuk pertukaran informasi antar sistem, namun JSON lebih populer dibandingkan XML karena beberapa alasan mendasar. JSON, subset dari JavaScript, memiliki struktur yang lebih sederhana dan langsung dibandingkan XML, sehingga JSON lebih mudah diproses dan digunakan langsung dalam JavaScript tanpa perlu melakukan parsing tambahan. JSON juga menghindari penggunaan tag yang panjang dan berlebihan seperti pada XML, sehingga ukuran data yang dikirimkan lebih kecil dan lebih efisien. Hal tersebut pun mengurangi overhead dalam transmisi data dan mempermudah pengelolaan memori dan CPU pada server.

Di sisi lain, XML memiliki aturan yang lebih ketat mengenai struktur dan format, seperti kepekaan huruf besar-kecil dan larangan penggunaan spasi dalam tag, yang dapat membuat pengolahan dan validasi XML lebih rumit. Selain itu, XML sering kali menghasilkan ukuran file yang lebih besar karena tag-tag deskriptif yang banyak. Karena format JSON lebih ringkas, JSON lebih cepat dan efisien dalam hal pertukaran data.


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

Dalam contoh kode saya di atas, jika form yang diterima dalam request POST valid, maka data produk baru akan disimpan ke database dan pengguna akan dialihkan ke halaman daftar produk. Jika form tidak valid, data tidak akan disimpan, dan form dengan error handling message akan ditampilkan kembali.


## Penggunaan `csrf_token` pada form di Django
`csrf_token` merupakan mekanisme keamanan dalam Django untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF), jenis cyberattack di mana situs web jahat dapat memaksa browser user untuk melakukan aksi yang tidak diinginkan di situs web yang tepercaya tanpa sepengetahuan user. Misalnya, jika user telah login ke situs web perbankan secara tidak sengaja mengunjungi situs web jahat, situs jahat tersebut bisa mengirimkan request untuk melakukan transfer dana tanpa izin. `csrf_token` mencegah hal tersebut terjadi dengan memastikan bahwa setiap request POST yang dikirim ke server termasuk token CSRF yang valid. Token ini hanya dapat diterbitkan oleh server dan hanya berlaku untuk sesi user tertentu, sehingga mencegah third-party yang tidak sah untuk memanipulasi request.

Jika `csrf_token` tidak ditambahkan ke form di Django, aplikasi web akan rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan kelemahan tersebut dengan membuat formulir yang tampaknya sah di situs mereka sendiri, yang saat dikirim dapat melakukan tindakan berbahaya di situs web target yang tidak dilindungi. Dengan mengaktifkan `csrf_token` dalam setiap form, Django memastikan bahwa hanya permintaan yang berasal dari sumber yang sah dan terpercaya yang dapat memodifikasi data atau melakukan aksi sensitif pada server.


## Screenshot pengaksesan keempat URL dengan Postman:
![Screenshot (1035)](https://github.com/user-attachments/assets/75841a93-c1bf-44f3-8da7-038c1adc51f1)
![Screenshot (1034)](https://github.com/user-attachments/assets/f22fcfac-79d3-4dd9-8876-d2452e94f367)
![Screenshot (1033)](https://github.com/user-attachments/assets/1c60e11a-7732-4464-bdf2-ffd0ad76bd81)
![Screenshot (1032)](https://github.com/user-attachments/assets/936ee3e4-4bd9-47cd-8d38-329bf5ccd767)
Dapat disimpulkan bahwa URL telah menghasilkan output yang diharapkan.
