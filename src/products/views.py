from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import CategoryForm, AuthorForm
from .models import Category, Author
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'dashboard/page/listview.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Get the count of all Category objects and add it to the context
        context['count'] = self.model.objects.count()
        # Add your custom context variables
        context['page_title'] = 'Category List'
        context['owner'] = 'category'
        return context

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

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'dashboard/page/single_data_form.html'
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Edit Category'
        context['owner'] = 'category'
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'dashboard/page/category_confirm_delete.html'
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Confirmation'
        return context
    
# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'dashboard/page/listview.html'
    context_object_name = 'authors'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.model.objects.count()
        # Add your custom context variables
        context['page_title'] = 'Author List'
        context['owner'] = 'author'
        return context
    
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
    
class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']
    template_name = 'dashboard/page/single_data_form.html'
    success_url = reverse_lazy('authors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Edit Author'
        context['owner'] = 'author'
        return context
    
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'dashboard/page/category_confirm_delete.html'
    success_url = reverse_lazy('authors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Confirmation'
        return context