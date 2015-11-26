from django.db import models

# Create your models here.

class Book( models.Model) :
    def __str__(self )  :
        return "Book( title: " + self.title + " , author_name: " + self.author_name+ " )"


    title = models.CharField( max_length=200)
    author_name = models.CharField( max_length = 200)

class Author( models.Model ) :
    def __str__( self ) :
        return "Author( name: " + self.name + " , books: " + str([ b.title for b in self.books.all()] )+ " )"

    name = models.CharField( max_length = 200  )
    books = models.ManyToManyField( Book)
