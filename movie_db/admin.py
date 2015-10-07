from django.contrib import admin
from .models import Status, Favorite

Class StatusAdmin(admin.ModelAdmin):

admin.site.register(Status, StatusAdmin)
admin.site.register(Favorite)
# Register your models here.
