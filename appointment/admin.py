from django.contrib import admin
from .models import Appointment, Genders
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Genders)