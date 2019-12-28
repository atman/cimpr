from django.contrib import admin
from . import models
from core.forms import ContactForm

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'type', 'phone_number', 'user']
    form = ContactForm

    #class Meta:
    #    model = models.Contact


admin.site.register(models.User)
admin.site.register(models.Contact, ContactAdmin)