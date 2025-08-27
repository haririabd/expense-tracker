from django.contrib import admin
from .models import Category, Author

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Category, CategoryAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Author, AuthorAdmin)