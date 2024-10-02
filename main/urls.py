from django.urls import path
from . import views
from main.views import tambah_produk, show_main, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_produk
from main.views import delete_produk

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
    path('edit-produk/<uuid:id>/', edit_produk, name='edit_produk'),
    path('delete-produk/<uuid:id>/', delete_produk, name='delete_produk'),
]