from django.contrib import admin

from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdminModel(admin.ModelAdmin):
    list_display=['name','email','password']
