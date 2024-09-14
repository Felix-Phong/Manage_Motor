from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class Category(models.Model):
    name = models.CharField(max_length=191,null=True)
    slug = models.CharField(max_length=191,null=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=0,null=True, blank=True)
    image = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  
    status = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderdetails = self.orderdetail_set.all()
        total = sum([orderdetail.get_total for orderdetail in orderdetails])
        return total
    def get_cart_items(self):
        orderdetails = self.orderdetail_set.all()
        total = sum([item.quantity for item in orderdetails])
        return total
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=191,null=True, blank=True)
    slug = models.CharField(max_length=191,null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    original_price = models.IntegerField(default=0,null=True, blank=True)
    selling_price = models.IntegerField(default=0,null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    qty = models.IntegerField(default=0,null=True, blank=True)
    status = models.IntegerField(default=0,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class OrderDetail(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    selling_price = models.IntegerField(default=0,null=True, blank=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    status = models.IntegerField(default=0,null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.original_price * self.quantity
        return total
