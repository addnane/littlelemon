from django.shortcuts import render,redirect
from rest_framework import generics
from .models import MenuTable,BookingTable
from .serializers import MenuTableSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset=MenuTable.objects.all()
    serializer_class = MenuTableSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuTable.objects.all()
    serializer_class=MenuTableSerializer

class Book(viewsets.ModelViewSet):
    queryset=BookingTable.objects.all()
    serializer_class=MenuTableSerializer
    permission_classes = [permissions.IsAuthenticated] 


def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})






