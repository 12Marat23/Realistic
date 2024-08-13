from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True  # 'Сохранить как', сохраняет как новый объект. По умолчанию - False.
    save_on_top = True  # 'Сохранить' наверху
    list_display = ('id', 'title', 'slug', 'category',
                    'created_at', 'get_photo', 'views')  # список полей отображающихся в админке.
    list_display_links = ('id', 'title')  # ссылка
    search_fields = ('title',)
    list_filter = ('category',)  # список фильтров
    readonly_fields = ('views', 'created_at', 'get_photo')  # список полей только для чтения.
    fields = ('title', 'slug', 'category',  'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" >')
        return '-'

    get_photo.short_description = 'Фото'


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
