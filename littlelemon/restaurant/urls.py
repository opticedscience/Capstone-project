from django.contrib import admin 
from django.urls import path ,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [ 
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('menu/', views.MenuItemView.as_view(), name='menuitem'),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view(), name='singlemenuitem'),
    path('api-token-auth/',obtain_auth_token),
]