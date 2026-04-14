from django.contrib import admin
from .models import student

# Register your models here.
class studentadmin(admin.ModelAdmin):
    model = student
    list_display = ['id','name','course','simage']

admin.site.register(student,studentadmin)
