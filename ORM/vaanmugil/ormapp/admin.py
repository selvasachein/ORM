from django.contrib import admin                                             
from .models import book,bookAdmin                                           
admin.site.register(book,bookAdmin)