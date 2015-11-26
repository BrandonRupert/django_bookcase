"""django_bookcase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url , patterns
from django.contrib import admin
import simplejson

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'books.views.about') ,
    url(r'^home/', 'books.views.home'),
    url(r'^books/', 'books.views.books'),
    url(r'^authors/', 'books.views.authors'),
    url(r'^book/(?P<book_pk>\d+)/$', 'books.views.book'),
    url(r'^author/(?P<author_pk>\d+)/$', 'books.views.author'),
    url(r'^delete_book/','books.views.delete_book') ,
    url(r'^new_author_book/', 'books.views.new_author_book') ,
    url(r'^delete_author/', 'books.views.delete_author'), 
)
