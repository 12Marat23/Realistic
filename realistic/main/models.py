from django.db import models
from django.urls import reverse


# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")  # name of the menu
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Ссылка")  # slug of the menu

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('index', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Article(models.Model):  # article model for blog
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    author = models.CharField(max_length=255, verbose_name='Автор')
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='articles')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})
