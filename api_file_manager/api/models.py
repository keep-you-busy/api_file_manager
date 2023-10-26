from django.db import models


class File(models.Model):
    file = models.FileField(
        verbose_name='Загруженный файл',
        upload_to='uploads/')
    uploaded_at = models.DateTimeField(
        verbose_name='Дата загрузки',
        auto_now_add=True,
        editable=False)
    processed = models.BooleanField(
        verbose_name='Статус обработки',
        default=False)
    content = models.TextField(
        verbose_name='Содержимое файла',
        default=''
    )

    def __str__(self):
        return f'{self.file.name}: {self.uploaded_at.date()}'
