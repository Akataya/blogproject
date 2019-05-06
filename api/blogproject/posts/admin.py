from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        list_display = ('title', 'author', 'created', 'published')

