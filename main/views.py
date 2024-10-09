import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def home(request):
    products = Product.objects.filter(user=request.user)  
    context = {
        'products': products,  
    }
    return render(request, "home.html", context)  

def tambah_produk(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle data POST dan FILES untuk gambar
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Set user to the logged-in user
            product.save()  # Save data product baru ke database
            return redirect('main:daftar_produk')  # Redirect ke page daftar produk 
    else:
        form = ProductForm()  # Buat form kosong kalau bukan POST

    return render(request, 'tambah-produk.html', {'form': form})  # Render form di template

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

@login_required(login_url='/login')
def daftar_produk(request):
    return render(request, 'daftar_produk.html')  # Render daftar produk

@login_required(login_url='/login')
def edit_produk(request, id):
    produk = get_object_or_404(Product, id=id)  # Ambil produk berdasarkan ID
    if produk.user != request.user:
        return HttpResponse('Unauthorized', status=401)  # Pastikan pengguna hanya dapat mengedit produk miliknya

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=produk)  # Load produk yang ada ke dalam form
        if form.is_valid():
            form.save()  # Simpan produk yang diperbarui
            return redirect('main:daftar_produk')  # Redirect ke daftar produk
    else:
        form = ProductForm(instance=produk)  # Populate form dengan data produk jika bukan POST

    return render(request, 'main/edit-produk.html', {'form': form})  # Render form edit

@login_required(login_url='/login')
def delete_produk(request, id):
    produk = get_object_or_404(Product, id=id)
    if produk.user != request.user:
        return HttpResponse('Unauthorized', status=401)  # Pastikan hanya pengguna yang memiliki produk yang bisa menghapus

    if request.method == "POST":
        produk.delete()  # Hapus produk
        return redirect('main:daftar_produk')

    return render(request, 'delete_produk.html', {'produk': produk})

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun kamu berhasil dibuat!')
            return redirect('main:login')
    return render(request, 'register.html', {'form': form})

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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)  # Ambil produk berdasarkan pengguna yang login
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
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    products = Product.objects.filter(user=request.user)
    data = list(products.values('id', 'nama', 'harga', 'deskripsi', 'stok', 'kategori', 'ukuran', 'warna', 'diskon', 'tanggal_dibuat', 'tanggal_diperbarui'))
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})  # Added indent for readability

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id).first()
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