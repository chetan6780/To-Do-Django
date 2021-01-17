from django.contrib import admin
from .models import Contact, Todo

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','textarea')


admin.site.register(Todo)
admin.site.register(Contact,ContactAdmin)