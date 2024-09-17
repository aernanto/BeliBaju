# Generated by Django 5.1.1 on 2024-09-17 17:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deskripsi',
            field=models.TextField(verbose_name='Deskripsi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='diskon',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Diskon'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='gambar_produk/', verbose_name='Gambar'),
        ),
        migrations.AlterField(
            model_name='product',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Harga'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='kategori',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nama',
            field=models.CharField(max_length=270, verbose_name='Nama Produk'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stok',
            field=models.PositiveIntegerField(default=0, verbose_name='Stok'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tanggal_dibuat',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tanggal Dibuat'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tanggal_diperbarui',
            field=models.DateTimeField(auto_now=True, verbose_name='Tanggal Diperbarui'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ukuran',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Ukuran'),
        ),
        migrations.AlterField(
            model_name='product',
            name='warna',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Warna'),
        ),
    ]
