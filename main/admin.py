from django.contrib import admin
from .models import Photo
# Register your models here.
class photoAdmin(admin.ModelAdmin):
	list_display = ["author", "short_description", "tag"]

admin.site.register(Photo, photoAdmin)