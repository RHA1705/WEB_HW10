from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quotes, Author, Tag

from .utils import get_mongodb


def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quotes.objects.all()
    per_page = 100
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def get_author(request, id):
    author = Author.objects.get(pk=id)
    print(author)
    return render(request, 'quotes/author.html', context={'author': author})