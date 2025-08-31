from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index_view(request, *args, **kwargs):
    page_title = 'Homepage'
    html_template = 'landingpage/page/index.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)

def about_view(request, *args, **kwargs):
    page_title = 'About'
    html_template = 'landingpage/page/book_list.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)

# Dashboard Views Start
@login_required
def dashboard_view(request, *args, **kwargs):
    page_title = 'Dashboard'
    html_template = 'dashboard/page/blank.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)

def blank_view(request, *args, **kwargs):
    page_title = 'Blank Page'
    html_template = 'dashboard/page/blank.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)