from django.contrib import admin
from app.models import URLMapper


@admin.register(URLMapper)
class URLMapperAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "shorten_url",)
    list_filter = ("create",)
