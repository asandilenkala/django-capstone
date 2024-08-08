from django.contrib import admin
from .models import Project

# Register your models here.
# This allows the Project model to be managed through the Django admin interface.
admin.site.register(Project)
