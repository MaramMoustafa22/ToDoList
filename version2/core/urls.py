import imp
from unicodedata import name
from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('update/<str:pk>/',views.update,name= 'update'),
    path('delete/<str:pk>/',views.delete,name= 'delete'),
    path('items/<str:pk>/',views.items,name='items'),
    path('new_item/<str:pk>/',views.new_item,name='new_item'),
    path('complete/<str:pk>/',views.completeTodo,name='complete')

]