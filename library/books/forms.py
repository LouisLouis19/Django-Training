# STEP 3: CREATE NEW FORM TO ADD BOOK TO RECORDS

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
