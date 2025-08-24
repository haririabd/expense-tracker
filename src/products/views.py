from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'landingpage/page/book_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'landingpage/page/category_form.html'
    success_url = reverse_lazy('categories')