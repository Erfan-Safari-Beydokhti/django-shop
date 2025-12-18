from django.db import models

# Create your models here.

class HomeSlider(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title')
    image=models.ImageField(upload_to='images/sliders',verbose_name='Image')
    link=models.URLField(blank=True,verbose_name='Link')
    is_active=models.BooleanField(default=True,verbose_name='Active')
    order=models.PositiveIntegerField(default=0,verbose_name='Order')

    class Meta:
        ordering=['order']
        verbose_name='Slider'
        verbose_name_plural='Sliders'
    def __str__(self):
        return self.title
