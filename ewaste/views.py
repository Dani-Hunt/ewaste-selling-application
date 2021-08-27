from django.shortcuts import redirect, render
from .models import Desktops, Laptops, Others, Phones
from django.contrib import messages
from django.views.generic import DetailView,UpdateView,DeleteView,ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
import json
from .models import *
from .decorators import authenticated_user

     
class PhonesDetailView(DetailView):
     model = Phones

class LaptopsDetailView(DetailView):
     model = Laptops

class OthersDetailView(DetailView):
     model = Others     


 
class PhonesCreateView(LoginRequiredMixin, CreateView):
     model = Phones 
     fields = ['name','description','image','price'] 

     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)


class PhonesUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
     model = Phones 
     fields = ['name','description','image','price'] 

     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)

     def test_func(self):
          phones = self.get_object()   
          if self.request.user == phones.author:
               return True
          return False       

class PhonesDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
     model = Phones    
     success_url = '/'
     def test_func(self):
          phones = self.get_object()   
          if self.request.user == phones.author:
               return True
          return False                        



class LaptopsCreateView(LoginRequiredMixin, CreateView):
     model = Laptops 
     fields = ['name','description','image','price'] 

     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)


class LaptopsUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
     model = Laptops 
     fields = ['name','description','image','price'] 

     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)

     def test_func(self):
          laptops = self.get_object()   
          if self.request.user == laptops.author:
               return True
          return False       

class LaptopsDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
     model = Laptops    
     success_url = '/'
     def test_func(self):
          laptops = self.get_object()   
          if self.request.user == laptops.author:
               return True
          return False                        


class OthersCreateView(LoginRequiredMixin, CreateView):
     model = Others 
     fields = ['name','description','image','price'] 

     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)


class OthersUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
     model = Others
     fields = ['name','description','image','price'] 

     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)

     def test_func(self):
          others = self.get_object()   
          if self.request.user == others.author:
               return True
          return False       

class OthersDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
     model = Others   
     success_url = '/'
     def test_func(self):
          others = self.get_object()   
          if self.request.user == others.author:
               return True
          return False                        




def home(request):
     return render(request,'ewaste/home.html')     

def about(request):    
     return render(request, 'ewaste/about.html')

def desktops(request) :
     context = {
          'desktops' : Desktops.objects.all()
     }

     return render(request, 'ewaste/desktops.html', context)  



def laptops(request):
     context = {
          'laptops' : Laptops.objects.all()
     }         
     return render(request, 'ewaste/laptops.html', context)
                 
def phones(request):
     context={
          'phones' : Phones.objects.all()
     }            
     return render(request, 'ewaste/phones.html', context)

def others(request):
     context= {
          'others' : Others.objects.all()
     }     
     return render(request, 'ewaste/others.html', context)



def updateItem(request):
     data = json.loads(request.body)
     productId = data['productId']
     action = data['action']
     print('Action:', action)
     print('productId:', productId)

     customer = request.user.customer
     product = Product.objects.get(id=productId)
     order, created = Order.objects.get_or_create(customer=customer)
     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

     if action == 'add' :
          orderItem.quantity = (orderItem.quantity +1 )
     elif action == 'remove' :
          orderItem.quantity = (orderItem.quantity -1)

     orderItem.save()

     if orderItem.quantity <= 0:
          orderItem.delete()

     return JsonResponse('Item was added', safe=False)

def cart(request):
     # order, created = Order.objects.get_or_create(customer=Customer)
     # items = order.orderitem_set.all()
     context = {}
     return render(request,'ewaste/cart.html', context)

     




