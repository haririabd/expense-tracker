from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'dashboard/page/categories.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Add your custom context variables
        context['page_title'] = 'Category List'
        return context

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'landingpage/page/category_form.html'
    success_url = reverse_lazy('categories')