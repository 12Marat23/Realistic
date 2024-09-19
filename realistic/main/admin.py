from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True
    list_display = ('title', 'slug')
    list_filter = ('title',)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category',
                    'created_at', 'get_photo', 'views')
    list_filter = ('title', 'category')
    search_fields = ('title',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" >')
        return '-'

    get_photo.short_description = 'Фото'


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
