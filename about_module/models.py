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

class TeamMember(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    job_title = models.CharField(max_length=100,verbose_name='Job Title')
    image=models.ImageField(upload_to='images/team_member',verbose_name='Image')
    twitter=models.URLField(verbose_name='Twitter',blank=True,null=True)
    instagram=models.URLField(verbose_name='Instagram',blank=True,null=True)
    linkedin=models.URLField(verbose_name='Linkedin',blank=True,null=True)
    facebook=models.URLField(verbose_name='Facebook',blank=True,null=True)

