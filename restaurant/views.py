from django.shortcuts import render
from rest_framework import generics
from .models import MenuTable,BookingTable
from .serializers import MenuTableSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
def index(request):
    return  render(request,"index.html",{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset=MenuTable.objects.all()
    serializer_class = MenuTableSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuTable.objects.all()
    serializer_class=MenuTableSerializer

class BookingView(viewsets.ModelViewSet):
    queryset=BookingTable.objects.all()
    serializer_class=MenuTableSerializer
    permission_classes = [permissions.IsAuthenticated] 






