from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Quotes, Author, Tag

from .utils import get_mongodb
from .forms import TagForm, AuthorForm, QuoteForm


def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quotes.objects.all()
    per_page = 200
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def get_author(request, id):
    author = Author.objects.get(pk=id)
    print(author)
    return render(request, 'quotes/author.html', context={'author': author})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_author.html', context={'form': form})
    return render(request, 'quotes/add_author.html', context={'form': AuthorForm()})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        print(form)
        if form.is_valid():

            # quote = form.save(commit=False)
            # print(quote)
            # quote.user = request.user
            # quote.save()
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_quote.html', context={'form': form})
    return render(request, 'quotes/add_quote.html', context={'form': QuoteForm()})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_tag.html', context={'form': form})
    return render(request, 'quotes/add_tag.html', context={'form': TagForm()})



