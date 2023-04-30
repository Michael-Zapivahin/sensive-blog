from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 50


admin.site.register(Post)
admin.site.register(Tag)
# admin.site.register(Comment)
