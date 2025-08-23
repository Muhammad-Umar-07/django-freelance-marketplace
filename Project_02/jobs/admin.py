from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'status', 'created_by', 'created_at', 'is_open')
    list_filter = ('status', 'is_open', 'created_at')
    search_fields = ('title', 'description')

# Register your models here.
