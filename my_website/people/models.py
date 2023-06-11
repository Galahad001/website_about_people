from django.urls import reverse
from django.db import models

class People(models.Model):
    title = models.CharField(max_length=250, verbose_name='Имя')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    images = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.CharField(max_length=250, verbose_name='Автор')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('businessman', kwargs={'p_id':self.pk})
    
    class Meta:
        verbose_name_plural = 'Известные люди'
        verbose_name = 'Известные люди'
        ordering = ['date_create', 'title']
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
    
# Create your models here.
