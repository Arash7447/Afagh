from django.urls import path
from .views import ListPageView, AddPageView, EditPageView, DeletePageView, PageDetailView

app_name = 'dynamicpage'

urlpatterns = [
    
    path('book/list/<str:dcrp>/', ListPageView.as_view(dcrp='book-dcrp'), name='list_page'),
    
    path('book/add/', AddPageView.as_view(), name='add_page'),
    
    path('book/edit/<int:pk>/', EditPageView.as_view(), name='edit_page'),
    
    path('book/delete/<int:pk>/', DeletePageView.as_view(), name='delete_page'),

    path('book/detail/<int:pk>/', PageDetailView.as_view(), name='page_detail'),

]
