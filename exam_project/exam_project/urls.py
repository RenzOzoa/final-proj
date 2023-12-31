from django.contrib import admin
from django.urls import path
from exam_app.views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
