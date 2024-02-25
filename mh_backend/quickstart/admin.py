from django.contrib import admin

from quickstart.models import Branch

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'operating_hours', 'waze_link', 'latitude', 'longitude')

# Register your models here.
admin.site.register(Branch, BranchAdmin)