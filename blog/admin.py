from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_at",)
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Post, PostAdmin)