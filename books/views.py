from django.shortcuts import render

# Create your views here.
from books.models import Book, Author
from django.http import HttpResponse, HttpResponseBadRequest, Http404

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render


#from django.utils import simplejson
import simplejson
#import nltk
#from nltk.corpus import wordnet as wn




def about( request ) :
    return render(request, "about.html", {})
def home(request ) :
    return render(request, "home.html", {})
def books( request):
    b = Book.objects.order_by('title')
    all_books = []
    for bb in b :
        book = {}
        book['title'] = bb.title
        book['author_name'] = bb.author_name
        book['author_pk'] = Author.objects.get( name = bb.author_name).pk
        book['pk'] = bb.pk
        all_books.append( book )
    return render(request, "books.html", {'all_books' : all_books})
def authors( request ) :
    a = Author.objects.order_by( 'pk')
    all_authors = []
    for aa in a :
        author = {}
        author['name'] = aa.name
        author['pk'] = aa.pk
        all_authors.append( author)

    return render(request, "authors.html", {'all_authors': all_authors})

def book( request, book_pk ) :
    b = Book.objects.get( pk = int(book_pk))
    a = Author.objects.get( name = b.author_name )
    book = {}
    book['title'] = b.title
    book['author'] = { 'name' : a.name, 'pk' : a.pk}
    return render( request, "book.html", {'book': [book]})

def author( request, author_pk) :
    a = Author.objects.get( pk = int(author_pk))
    author = {}
    author['name'] = a.name
    author['books'] = []
    for b in Book.objects.filter( author_name = a.name ) :
        x = { 'title' : b.title , 'pk' : b.pk }
        author['books'].append( {'title': b.title, 'pk':b.pk})
    return render( request, "author.html", {'author': [author]})

@csrf_exempt
def delete_author( request ) :
    """
    Delete Author and all associated Books
    """
    json_data = simplejson.loads(request.body)
    author_pk = int( json_data['author_pk'])
    a = Author.objects.get( pk =author_pk )
    for b in Book.objects.filter( author_name = a.name ) :
        b.delete()
    a.delete()

    return HttpResponse("Success")

@csrf_exempt
def delete_book( request ) :

    """
    Delete Book. Author remains
    """
    json_data = simplejson.loads(request.body)
    book_pk = int( json_data['book_pk'])
    b = Book.objects.get( pk = book_pk)
    b.delete()

    return HttpResponse("Success")


@csrf_exempt
def new_author_book(request ) :
    json_data = simplejson.loads( request.body )
    book_title = json_data['title']
    name = json_data['name']
    if not Book.objects.filter( title=book_title, author_name=name).exists() :
        b = Book( title = book_title, author_name = name )
        b.save()
    else :
        return HttpResponse("Success")
    author_name = name
    if Author.objects.filter( name = author_name ).exists() :
        a = Author.objects.get( name = author_name)
        a.books.add( b )
        a.save()
    else :
        a = Author(name = author_name )
        a.save()
        a.books.add( b)
        a.save()
    return HttpResponse("Success")
