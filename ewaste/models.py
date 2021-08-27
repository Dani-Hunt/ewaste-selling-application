from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse


def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('phones-detail')
    

class Laptops(models.Model):
    name = models.CharField(default=('electronic'), max_length=30) 
    description = models.TextField(max_length=50)
    image = models.ImageField(default = 'defaultlaptop.jpg', upload_to = 'laptop_pics')
    price = models.CharField(default='$' ,max_length=10)
    author = models.ForeignKey(User, default = '',null=False ,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('laptops-detail', kwargs={'pk': self.pk})

class Phones(models.Model):
    name = models.CharField(default=('electronic'), max_length=30) 
    description = models.TextField(max_length=50)
    image = models.ImageField(default = 'defaultphone.jpg',null=False, upload_to = 'phone_pics')
    price = models.CharField(default='$' ,max_length=10)
    author = models.ForeignKey(User, default = '' ,null=False,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phones-detail', kwargs={'pk': self.pk})

class Others(models.Model):
    name = models.CharField(default=('electronic'), max_length=30) 
    description = models.TextField(max_length=50)
    image = models.ImageField(default = 'defaultother.jpg', upload_to = 'other_pics')
    price = models.CharField(default='$' ,max_length=10)    
    author = models.ForeignKey(User, default = '',null=False ,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('others-detail', kwargs={'pk': self.pk})


class Desktops(models.Model):
    name = models.CharField(default=('electronic'), max_length=30) 
    description = models.TextField(max_length=50)
    image = models.ImageField(default = 'defaultdesktop.jpg', upload_to = 'desktop_pics')
    price = models.CharField(default='$' ,max_length=10)
    author = models.ForeignKey(User, default = '' ,null=False,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Phones, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)