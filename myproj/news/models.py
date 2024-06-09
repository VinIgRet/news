from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class News(models.Model):

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    title = models.CharField(max_length=100,verbose_name='Заголовок')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлено')
    content = models.TextField(blank=True, null=True,verbose_name='Контент')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True,verbose_name='Фото')
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')
    category = models.ForeignKey('NewsCategory', on_delete=models.PROTECT,null=True,verbose_name='Категория') 
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('newsdetail', kwargs={'newsid': self.pk}) 

class NewsCategory(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('catnews', kwargs={'catid': self.pk})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']