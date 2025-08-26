from django.db import models
from django import forms
from django.forms import ClearableFileInput

# Create your models here.
class uploadCSV(models.Model):
    file = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class uploadCSVForm(forms.ModelForm):
    class Meta:
        model = uploadCSV
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={
                'class': "form-control"
            })
        }