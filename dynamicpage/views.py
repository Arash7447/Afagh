from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Page
from .serializers import PageSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class ListPageView (ListView):
   
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'
    page_size = 4
    dcrp = None

    def get_queryset (self):
        
        queryset = super().get_queryset()
        title = self.request.GET.get ('title')
        content = self.request.GET.get ('content')

        if title:
            queryset = queryset.filter (title__icontains=title)
        if content:
            queryset = queryset.filter (content__icontains=content)

        paginator = Paginator(queryset, self.page_size)
        page_number = self.request.GET.get('page')

        try:
            queryset = paginator.page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return queryset


class PageDetailView (DetailView):
    model = Page
    template_name = 'pages/detail.html'

    def get_success_url(self):
        return reverse('dynamicpage:list_page', kwargs={'dcrp': 'book-dcrp'})



class AddPageView (CreateView):    
    model = Page
    template_name = 'pages/add.html'
    fields = ('title', 'content')
    success_url = '/book/list/book-dcrp/'


class EditPageView(UpdateView):
    model = Page
    template_name = 'pages/edit.html'
    fields = ('title', 'content')
    success_url = '/book/list/book-dcrp/' 


class DeletePageView (DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = '/book/list/book-dcrp/' 




