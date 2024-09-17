from django.urls import path
from . import views
from main.views import tambah_produk, show_main, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'), 
    path('tambah-produk/', views.tambah_produk, name='tambah_produk'),  
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
]