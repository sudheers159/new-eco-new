from django.contrib import admin
from django.db import models
from .models import Category, Product,Student,Contact_Us, Contact,Category_New, register_table
import datetime

# Register your models here.


admin.site.site_header="My Website | Second Project"

class StudentAdmin(admin.ModelAdmin):
    # fields=["name", "email", "roll_no"]
    list_display=["name", "roll_no", "email", "fee", "is_registered"]
    search_fields=["roll_no"]
    list_filter=['name']
    list_editable=['email']

class Contact_UsAdmin(admin.ModelAdmin):
    # fields=["name", "email", "time"]
    list_display=["name", "email", "time",]
    search_fields=["email"]
    list_filter=['name']
    list_editable=['email']



admin.site.register(Product)
admin.site.register(Category)   
admin.site.register(Contact_Us,Contact_UsAdmin)
admin.site.register(Student,StudentAdmin)   
admin.site.register(Contact)   
admin.site.register(Category_New)
admin.site.register(register_table)






