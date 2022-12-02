from django.contrib import admin
from .models import Category, News
from .models import Like #import the class from models file present in the app

# Register your models here.

admin.site.register(Like)

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display = ('title','category')

admin.site.register(News, AdminNews)