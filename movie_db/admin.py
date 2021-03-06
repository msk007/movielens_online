from django.contrib import admin
from .models import Movie, User_id, Rating






class UserAdmin(admin.ModelAdmin):
    list_display =['user_id', 'gender']


class MovieAdmin(admin.ModelAdmin):
    list_display =['movie_id']


class RatingAdmin(admin.ModelAdmin):
    list_display =['user_id','movie_id','rating']

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(User_id, UserAdmin)
admin.site.register(Rating, RatingAdmin)
