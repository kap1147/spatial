from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Post

@admin.register(Post)
class PostAdmin(OSMGeoAdmin):
    list_display = ('title', 'location', 'timestamp')
