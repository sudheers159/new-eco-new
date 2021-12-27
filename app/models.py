from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='product/')

    def __str__(self):
        return f"{'name'} {'price'}"
class Category(models.Model):
    cat=models.ForeignKey(Product , on_delete=models.CASCADE)


class Student(models.Model):
    c=(
        ("M","Male"), ("F","Female")
    )
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    roll_no=models.IntegerField(unique=True)
    fee=models.FloatField()
    address=models.TextField()
    gender=models.CharField(max_length=150, choices=c)
    is_registered=models.BooleanField()


    def __str__(self):
        return self.name+' '+self.address
        

class Contact_Us(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Feedback'

class Contact(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    subject=models.CharField(max_length=100)
    msg=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        

class Category_New(models.Model):
    name=models.CharField(max_length=200)
    cover_pic=models.FileField(upload_to="category/%Y/%m/%d")  
    description=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.name}"

class register_table(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.IntegerField()
    profile_pic=models.ImageField(upload_to="prifile/%y/%m/%d" , null=True)
    age=models.CharField(max_length=100, null=True, blank=True)
    city=models.CharField(max_length=100, null=True, blank=True)
    about=models.TextField( null=True, blank=True)
    gender=models.CharField(max_length=100, blank=True, default="Male")
    occupation=models.CharField(max_length=100, null=True, blank=True)
    added_on=models.DateTimeField(auto_now_add=True, null=True)
    update_on=models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return f"{self.user.username}"
        

        
