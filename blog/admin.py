from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
