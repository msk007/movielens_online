from django.contrib import admin
from .models import Movie, User_id, Rating





# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
