from django.db import models                                                                                                                      
from django.contrib import admin                                             
class book(models.Model):                    				      
   bookno=models.IntegerField(primary_key=True);                                                      
   authorname=models.CharField(max_length=50);                                                            
   price=models.IntegerField(help_text="enter price");                       
   qty=models.IntegerField();                                                
   bookname=models.CharField(max_length=50);                                 
class bookAdmin(admin.ModelAdmin):                                           
   list_display=("bookno","authorname","price","qty","bookname"); 