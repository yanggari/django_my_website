from django.contrib import admin
from . models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','title','created','author']
    list_display_links = ['title']
admin.site.register(Post,PostAdmin)

