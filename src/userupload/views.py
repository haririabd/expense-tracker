from django.shortcuts import render, redirect, HttpResponseRedirect
from .user_upload import upload_file
from django.contrib import messages
from products.models import Category, Author
from .models import uploadCSVForm
from django.urls import reverse_lazy
import chardet
import csv

# chunk_size = 1000

# Create your views here.
def upload_csv(request, model_name):
    # Map the model name from URL to actual django model and set the required parameters
    model_map = {
        'category': {'model': Category, 'redirect_url': 'categories', 'owner': 'category'},
        'author': {'model': Author, 'redirect_url': 'authors', 'owner': 'author'}
    }
    
    # Check if the requested model name is valid
    if model_name not in model_map:
        messages.error(request, 'Invalid upload type.')
        return redirect('index')
    
    # Get the correct model and redirect link from the map
    target_model = model_map[model_name]['model']
    redirect_url_name = model_map[model_name]['redirect_url']
    owner = model_map[model_name]['owner']
    
    page_title = 'Bulk Upload'
    if request.method == 'POST':
        form = uploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']
            file_path = upload_file(csv_file)  # Call the upload_file function
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip the header row
                    
                    for row in reader:
                        item_name = row[0]
                        # Dynamically get or create the object for the specified model
                        target_model.objects.get_or_create(name=item_name)
                        
                messages.success(request, 'File uploaded successfully!')
            except:
                messages.error(request, 'An encoding error occurred, but the file was proccessed. Some characters may be missing')    
            return HttpResponseRedirect(reverse_lazy(redirect_url_name))
        
        else:
            form = uploadCSVForm()
            context = {
                'form': form,
                'page_title': page_title,
                'owner': owner
            }
            return(request, 'dashboard/page/userupload.html', context)
    
    else:
        form = uploadCSVForm()
        context = {
            'form': form,
            'page_title': page_title,
            'owner': owner
        }
        return render(request, 'dashboard/page/userupload.html', context)

# def add_category_csv(request):
#     page_title = 'Bulk Upload'
    
#     if request.method == 'POST':
#         form = uploadCSVForm(request.POST, request.FILES)

#         if form.is_valid():
#             csv_file = request.FILES['file']
#             file_path = upload_file(csv_file)  # Call the upload_file function
            
#             with open(file_path, 'r') as f:
#                 categories = []
#                 reader = csv.reader(f)
#                 next(reader)  # Skip the header row
#                 for row in reader:
#                     category_name = row[0]
#                     # categories.append({'category': str(category)})
                    
#                     category, created = Category.objects.get_or_create(name=category_name)
                    
#             messages.success(request, 'File uploaded successfully!')
#             # print(categories)
            
#             return HttpResponseRedirect(reverse_lazy('categories'))
#         else:
#             form = uploadCSVForm()
#             context = {
#                 'form': form,
#                 'page_title': page_title
#             }
#             return(request, 'dashboard/page/userupload.html', context)
    
#     else:
#         form = uploadCSVForm()
#         context = {
#             'form': form,
#             'page_title': page_title
#         }
#         return render(request, 'dashboard/page/userupload.html', context)

# def add_author_csv(request):
#     page_title = 'Bulk Upload'
    
#     if request.method == 'POST':
#         form = uploadCSVForm(request.POST, request.FILES)

#         if form.is_valid():
#             csv_file = request.FILES['file']
#             file_path = upload_file(csv_file)  # Call the upload_file function
            
#             with open(file_path, 'r') as f:
#                 authors = []
#                 reader = csv.reader(f)
#                 next(reader)  # Skip the header row
#                 for row in reader:
#                     author_name = row[0]
#                     # categories.append({'category': str(category)})
                    
#                     author, created = Author.objects.get_or_create(name=author_name)
                    
#             messages.success(request, 'File uploaded successfully!')
#             # print(authors)
            
#             return HttpResponseRedirect(reverse_lazy('authors'))
#         else:
#             form = uploadCSVForm()
#             context = {
#                 'form': form,
#                 'page_title': page_title
#             }
#             return(request, 'dashboard/page/userupload.html', context)
    
#     else:
#         form = uploadCSVForm()
#         context = {
#             'form': form,
#             'page_title': page_title
#         }
#         return render(request, 'dashboard/page/userupload.html', context)