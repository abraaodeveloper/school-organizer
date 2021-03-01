from django.contrib import admin
from s_organizer_api.models import User

# Register your models here.
class Users(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = [ 'id', 'name']
    search_fields = ['name' ]

admin.site.register(User, Users)