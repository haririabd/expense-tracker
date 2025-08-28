from django.shortcuts import render, HttpResponseRedirect
from .user_upload import upload_file
from django.contrib import messages
from products.models import Category, Author
from .models import uploadCSVForm
from django.urls import reverse_lazy
import csv

# Create your views here.
def add_category_csv(request):
    page_title = 'Bulk Upload'
    
    if request.method == 'POST':
        form = uploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']
            file_path = upload_file(csv_file)  # Call the upload_file function
            
            with open(file_path, 'r') as f:
                categories = []
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    category_name = row[0]
                    # categories.append({'category': str(category)})
                    
                    category, created = Category.objects.get_or_create(name=category_name)
                    
            messages.success(request, 'File uploaded successfully!')
            # print(categories)
            
            return HttpResponseRedirect(reverse_lazy('categories'))
        else:
            form = uploadCSVForm()
            context = {
                'form': form,
                'page_title': page_title
            }
            return(request, 'dashboard/page/userupload.html', context)
    
    else:
        form = uploadCSVForm()
        context = {
            'form': form,
            'page_title': page_title
        }
        return render(request, 'dashboard/page/userupload.html', context)

def add_author_csv(request):
    page_title = 'Bulk Upload'
    
    if request.method == 'POST':
        form = uploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']
            file_path = upload_file(csv_file)  # Call the upload_file function
            
            with open(file_path, 'r') as f:
                authors = []
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    author_name = row[0]
                    # categories.append({'category': str(category)})
                    
                    author, created = Author.objects.get_or_create(name=author_name)
                    
            messages.success(request, 'File uploaded successfully!')
            # print(authors)
            
            return HttpResponseRedirect(reverse_lazy('authors'))
        else:
            form = uploadCSVForm()
            context = {
                'form': form,
                'page_title': page_title
            }
            return(request, 'dashboard/page/userupload.html', context)
    
    else:
        form = uploadCSVForm()
        context = {
            'form': form,
            'page_title': page_title
        }
        return render(request, 'dashboard/page/userupload.html', context)