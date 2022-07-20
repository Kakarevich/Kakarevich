from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255) # класс CharField определяет макс длину текстового поля
    content = models.TextField(blank=True) # blank=True позволяет поле оставить пустым
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/") # хполе хранит ссылку на фото
    time_create = models.DateTimeField(auto_now_add=True) # поле с указанием времени создания статьи
    time_update = models.DateTimeField(auto_now=True) # поле с указанием времени редактирования статьи
    is_published = models.BooleanField(default=True) # булевое значение