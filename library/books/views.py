# STEP 4: IMPLEMENT YOUR LOGIC

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# def book_delete(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     book.delete()
#     return redirect('book_list')
