from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
