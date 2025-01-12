from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'message')  # Display these fields in admin


admin.site.register(Contact)

