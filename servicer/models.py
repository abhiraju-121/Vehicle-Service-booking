from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField()

    def __str__(self):
        return self.user.username

class Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField()
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)  # For sale
    description = models.TextField()
    owner=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='vehicles',default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.name} - ${self.price}"
    
class Cars(models.Model):
    user=models.ForeignKey(Staff,on_delete=models.CASCADE,default=True)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/')
    price=models.DecimalField(decimal_places=2,max_digits=10)
    desc=models.TextField()

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    purchase_date=models.DateTimeField(default=now)
    status=models.CharField(max_length=20,choices=[('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected')],default='Pending')


class Booking(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    service_date=models.DateField()
    service_time=models.TimeField()
    status=models.CharField(max_length=20,choices=[('Approved','Approved'),('Rejected','Rejected'),('Pending','Pending')],default='Pending')
    comment=models.TextField(blank=True,null=True)
