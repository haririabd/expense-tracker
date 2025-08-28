"""
URL configuration for arvmain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from userupload.views import add_category_csv, add_author_csv
from . import views
from products.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

ON_CODESPACE = settings.ON_CODESPACE

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Allauth path
    path('accounts/', include('allauth.urls')),
     # Application
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    # Adding Data
    path('add-category/', CategoryCreateView.as_view(), name='add-category'),
    path('add-author/', AuthorCreateView.as_view(), name='add-author'),
    # Edit Data
    path('edit-category/<int:pk>/', CategoryUpdateView.as_view(), name='edit-category'),
    path('edit-author/<int:pk>/', AuthorUpdateView.as_view(), name='edit-author'),
    # Delete Data
    path('delete-category/<int:pk>/', CategoryDeleteView.as_view(),name='delete-category'),
    path('delete-author/<int:pk>/', AuthorDeleteView.as_view(),name='delete-author'),
    # user upload
    path('add-category/upload/', add_category_csv, name='add-category-csv'),
    path('add-author/upload/', add_author_csv, name='add-author-csv'),
    # Sample Page
    path('blank/', views.blank_view, name='blank'),
]

if ON_CODESPACE:
    urlpatterns += [
        path('__reload__/', include("django_browser_reload.urls")),
    ]