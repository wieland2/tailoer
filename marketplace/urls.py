from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('products/create', views.createProduct, name="create-product"),
    path('products/<str:pk>', views.product, name="product"),
    path('products/edit/<str:pk>', views.editProduct, name="edit-product"),
    path('products/delete/<str:pk>', views.deleteProduct, name="delete-product"),
]
