from django.contrib import admin

from .models import Post, Comment

admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'date_added')

admin.site.register(Comment, CommentAdmin)
