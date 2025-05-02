from django.contrib import admin 
from django.urls import path ,include
from . import views



urlpatterns = [ 
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('menu/', views.MenuItemView.as_view(), name='menuitem'),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view(), name='singlemenuitem'),
]