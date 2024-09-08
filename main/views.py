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
