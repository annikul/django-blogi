from django.contrib import admin

# Register your models here.
from .models import Postaus

@admin.register(Postaus)
class PostausAdmin(admin.ModelAdmin):
    list_display = ['otsikko', 'luotu'] 
