
from django.core.exceptions import ValidationError
from django import forms
from .models import *

class PeopleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = People
        fields = ['title', 'content', 'is_published', 'cat']
        widgets = {
            'content':forms.Textarea(attrs={'cols':60, 'rows':10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')   
        
        return title
