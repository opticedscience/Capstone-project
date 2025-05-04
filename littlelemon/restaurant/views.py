from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,DestroyAPIView
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
# Create your views here.


# def sayHello(request):
#    return HttpResponse('Hello World')

def index(request):
  return render(request, 'index.html', {})

def home(request):
  return render(request, 'home.html',{})

class MenuItemView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [IsAdminUser]
    #     return [AllowAny]

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    permission_classes = [AllowAny]
    queryset=Menu.objects.all()
    serializer_class = MenuSerializer
    # def get_permissions(self):
    #     if self.request.method == 'POST' or self.request.method == 'Put' or self.request.method == 'DELETE':
    #         return [IsAdminUser]
    #     return [AllowAny]

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    