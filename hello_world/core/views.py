
from ..models import Book
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Book

def index(request):
    book = Book
    context = {
        "title": "Django example",
        "book": book
    }
    return render(request, "index.html", context)


@csrf_exempt
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                published_date=data['published_date'],
                isbn=data['isbn'],
                price=data['price'],
                stock_quantity=data['stock_quantity']
            )
            return JsonResponse({'id': book.id})
        else:
            book = Book.objects.create(
                title=request.POST['title'],
                author=request.POST['author'],
                published_date=request.POST['published_date'],
                isbn=request.POST['isbn'],
                price=request.POST['price'],
                stock_quantity=request.POST['stock_quantity']
            )
            return redirect('add_book')
    else:
        return render(request, 'add_book.html')