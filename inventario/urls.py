from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home ),
    path('proveedores', views.Proveedores),
    path('addProduct/', views.AddProduct),
    path('addEmb/', views.AddEmb),
    path('deleteProduct/<id>', views.DeleteProduct),
    path('editProduct/<id>', views.EditProduct),
    path('updateProduct/', views.UpdateProduct),
    path('addProvider/', views.AddProvider),
    path('deleteProvider/<id>', views.DeleteProvider),
    path('editProvider/<id>', views.EditProvider),
    path('updateProvider/', views.UpdateProvider),
    path('kardex', views.Registros)
]