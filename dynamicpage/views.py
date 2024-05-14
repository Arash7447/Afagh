from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Page

# Create your views here.

class ListPageView (ListView):
   
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'
    paginate_by = 5
    dcrp = None

    def get_queryset (self):
        
        queryset = super().get_queryset()
        title = self.request.GET.get ('title')
        content = self.request.GET.get ('content')

        if title:
            queryset = queryset.filter (title__icontains=title)
        if content:
            queryset = queryset.filter (content__icontains=content)

        return queryset


class PageDetailView (DetailView):

    model = Page
    template_name = 'pages/detail.html'



class AddPageView (CreateView):
    
    model = Page
    template_name = 'pages/add.html'
    fields = ('title', 'content')


class EditPageView(UpdateView):
    model = Page
    template_name = 'pages/edit.html'
    fields = ('title', 'content')
    success_url = '/book/list/book-dcrp/' 



class DeletePageView (DeleteView):
    
    model = Page
    template_name = 'pages/delete.html'
    success_url = '/book/list/book-dcrp/' 
