# Ex02 Django ORM Web Application
## Date:14-10-2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import blinkit,blinkitadmin
admin.site.register(blinkit,blinkitadmin)

models.py
from django.db import models
from django.contrib import admin 
class blinkit(models.Model):
    Name=models.CharField(max_length=10)
    Address=models.TextField()
    Delvivery_Id=models.IntegerField()
    Productname=models.CharField(max_length=10)
    Quantity=models.IntegerField()
    price=models.IntegerField()
    Mobile_Number=models.IntegerField(primary_key=True)
    

class blinkitadmin(admin.ModelAdmin):
    list_display=["Name","Address","Delvivery_Id","Productname","Quantity","price","Mobile_Number"]
```



## OUTPUT
<img width="1916" height="1077" alt="image" src="https://github.com/user-attachments/assets/d598f4c5-08d2-4c58-a317-4275cdf349e8" />




## RESULT
Thus the program for creating vehicle service Database using ORM hss been executed successfully.
