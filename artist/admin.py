from django.contrib import admin
from .models import Paint

class PaintAdmin(admin.ModelAdmin):
    list_display=['pk','title','is_active']

admin.site.register(Paint,PaintAdmin)
