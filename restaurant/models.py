from django.db import models

# Create your models here.
class BookingTable(models.Model):
    Id_number=models.IntegerField()
    Name=models.CharField(max_length=100)
    No_of_guests=models.IntegerField(max_length=100)
    BookingDate=models.DateField()




class MenuTable(models.Model):
    ID=models.IntegerField()
    Title=models.CharField(max_length=100)
    Price=models.DecimalField(decimal_places=2,max_digits=10)
    Inventory=models.IntegerField()