from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "categories"
        
class Author(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return str(self.name)