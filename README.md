Nama: Aimee C. F. P. Ernanto

NPM: 2306165963

Kelas: PBP C

Link PWS: 

E-Commerce: Clothing

Nama e-commerce: BeliBaju

**Langkah Pertama**
- Pertama-tama, saya telah membuat direktori baru di github dan direktori lokal.
- Untuk membuat proyek Django BeliBaju, saya kemudian membuka command prompt dan menjalankan ```django-admin startproject ecommerce_belibaju```.
- Saya selanjutnya menginisialisasi Git pada command prompt, ```git init```.
- Dengan bantuan Chat GPT (karena saya tidak tahu cara membuat .gitignore dalam satu line di command prompt), saya kemudian menambahkan berkas .gitignore agar git tidak mengacak-acak (bukan SIAK NG..) file dan direktori yang berisi ```echo "# Django\n*.log\n*.pot\n*.pyc\n__pycache__\ndb.sqlite3\nmedia\n\n# Backup files\n*.bak\n\n# If you are using PyCharm\n# User-specific stuff\n.idea/**/workspace.xml\n.idea/**/tasks.xml\n.idea/**/usage.statistics.xml\n.idea/**/dictionaries\n.idea/**/shelf\n\n# AWS User-specific\n.idea/**/aws.xml\n\n# Generated files\n.idea/**/contentModel.xml\n.DS_Store\n\n# Sensitive or high-churn files\n.idea/**/dataSources/\n.idea/**/dataSources.ids\n.idea/**/dataSources.local.xml\n.idea/**/sqlDataSources.xml\n.idea/**/dynamic.xml\n.idea/**/uiDesigner.xml\n.idea/**/dbnavigator.xml\n\n# Gradle\n.idea/**/gradle.xml\n.idea/**/libraries\n\n# File-based project format\n*.iws\n\n# IntelliJ\nout/\n\n# JIRA plugin\natlassian-ide-plugin.xml\n\n# Python\n*.py[cod]\n*$py.class\n\n# Distribution / packaging\n.Python build/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\n*.egg-info/\n.installed.cfg\n*.egg\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.coverage\n.coverage.*\n.cache\n.pytest_cache/\nnosetests.xml\ncoverage.xml\n*.cover\n.hypothesis/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# pyenv\n.python-version\n\n# celery\ncelerybeat-schedule.*\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n\n# Sublime Text\n*.tmlanguage.cache\n*.tmPreferences.cache\n*.stTheme.cache\n*.sublime-workspace\n*.sublime-project\n\n# sftp configuration file\nsftp-config.json\n\n# Package control specific files Package\nControl.last-run\nControl.ca-list\nControl.ca-bundle\nControl.system-ca-bundle\nGitHub.sublime-settings" > .gitignore```
- Saya kemudian melakukan ```git add .``` dan ```git commit -m "Tugas 2 First Commit```.
- Tak lupa, saya menghubungkan repositori lokal dengan GitHub saya dengan melakukan ```git remote add origin https://github.com/aernanto/Tugas2PBP.git```.
- Sebagai penutup langkah pertama, saya tak lupa untuk melakukan push, ```git push -u origin main```.

**Langkah Kedua**
- Karena saya telah membuat direktori proyek Django, dengan saya telah berada di direktori yang tepat, saya membuat app bernama main dengan cara ```python manage.py startapp main```.
- Saya menambahkan main ke dalam INSTALLED_APPS pada settings.py sebagai berikut:
``` 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
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
- 




