from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'exam_app/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductCreateView(CreateView):
    model = Product
    template_name = 'exam_app/product_form.html'
    fields = ['name', 'description', 'price', 'category']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'exam_app/product_form.html'
    fields = ['name', 'description', 'price', 'category']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'exam_app/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')
