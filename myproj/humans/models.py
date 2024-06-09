from django.db import models
from django.urls import reverse_lazy
# Create your models here.
class Humans(models.Model):

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Люди'
        ordering = ['famil', 'name', 'otches']
    
    nicname = models.CharField(max_length=50,verbose_name='Никнейм')
    famil = models.CharField(max_length=40,verbose_name='Фамилия')
    name = models.CharField(max_length=40,verbose_name='Имя')
    otches = models.CharField(max_length=40,blank=True, null=True,verbose_name='Отчество')   
    birthday = models.DateField(blank=True, null=True,verbose_name='День рождения')
    avatar = models.ImageField(upload_to='images/', blank=True, null=True,verbose_name='Аватарка')
    ismale=models.BooleanField(default=True,verbose_name='Мужчина')
    profession=models.ForeignKey('Professions', on_delete=models.PROTECT,null=True,verbose_name='Профессия')
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('humansdetail', kwargs={'humansid': self.pk})

class Professions(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy('profhumans', kwargs={'profid': self.pk})
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['title']