from rest_framework.serializers import ModelSerializer
from .models import MenuTable,BookingTable

class MenuTableSerializer(ModelSerializer):
    class Meta:
     model=MenuTable
     fields="__all__"




class BookingTableSerializer(ModelSerializer):
    class Meta:
     model=BookingTable
     fields="__all__"

    
