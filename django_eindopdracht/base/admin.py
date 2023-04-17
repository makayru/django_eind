from django.contrib import admin
from .models import Profile, Book, Read
# Register your models here.
# tested 
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Read)