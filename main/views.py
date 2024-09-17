from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, JsonResponse
from django.core import serializers

def tambah_produk(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle data POST dan FILES untuk gambar
        if form.is_valid():
            form.save()  # Save data product baru ke database
            return redirect('daftar_produk')  # Redirect ke page daftar produk 
    else:
        form = ProductForm()  # Buat form kosong kalau bukan POST

    return render(request, 'tambah-produk.html', {'form': form})  # Render form di template

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

def show_xml(request):
    data = Product.objects.all()  # Mengambil semua data dari model Product
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")  

def show_json(request):
    products = Product.objects.all()
    data = list(products.values('id', 'nama', 'harga', 'deskripsi', 'stok', 'kategori', 'ukuran', 'warna', 'diskon', 'tanggal_dibuat', 'tanggal_diperbarui'))
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})  # Added indent for readability

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)  # Mengambil data Product berdasarkan id
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

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