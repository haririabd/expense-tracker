from django.shortcuts import render, HttpResponseRedirect
from .user_upload import upload_file
from django.contrib import messages
from .models import uploadCSVForm
import csv

# Create your views here.
def add_category_csv(request):
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
                    category = row
                    categories.append({'category': str(category)})

            m = messages.success(request, 'File uploaded successfully!')
            context = {
                'categories': categories
            }
            return render(request, 'dashboard/page/categories.html', context)
        else:
            form = uploadCSVForm()
            context = {
                'form': form
            }
            return(request, context)
    
    else:
        form = uploadCSVForm()
        context = {
            'form': form,
        }
        return render(request, 'dashboard/page/userupload.html', context)