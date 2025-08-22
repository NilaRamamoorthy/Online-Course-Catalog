from django.contrib import admin

# Register your models here.
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')
    list_filter = ('level',)
    search_fields = ('title',)
