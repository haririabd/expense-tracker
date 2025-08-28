from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import CategoryForm, AuthorForm
from .models import Category, Author
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Base Views
class BaseListView(ListView):
    template_name = 'dashboard/page/listview.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.model.objects.count()
        context['page_title'] = self.page_title
        context['owner'] = self.owner
        return context

class BaseUpdateView(UpdateView):
    fields = ['name']
    template_name = 'dashboard/page/single_data_form.html'
    page_title = ''
    owner = ''
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['owner'] = self.owner
        return context

class CategoryListView(BaseListView):
    model = Category
    context_object_name = 'categories'
    page_title = 'Category List'
    owner = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm # Link with form we created in forms.py so we can edit the style
    template_name = 'dashboard/page/single_data_form.html'
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Category'
        context['owner'] = 'category'
        return context
    
class CategoryUpdateView(BaseUpdateView):
    model = Category
    success_url = reverse_lazy('categories')
    page_title = 'Edit Category'
    owner = 'category'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'dashboard/page/category_confirm_delete.html'
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Confirmation'
        return context
    
# Author Views
class AuthorListView(BaseListView):
    model = Author
    context_object_name = 'authors'
    page_title = 'Author List'
    owner = 'author'
    
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm # Link with form we created in forms.py so we can edit the style
    template_name = 'dashboard/page/single_data_form.html'
    success_url = reverse_lazy('authors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Author'
        context['owner'] = 'author'
        return context
    
class AuthorUpdateView(BaseUpdateView):
    model = Author
    success_url = reverse_lazy('authors')
    page_title = 'Edit Author'
    owner = 'author'
    
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'dashboard/page/category_confirm_delete.html'
    success_url = reverse_lazy('authors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Confirmation'
        return context