from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    site_name=models.CharField(max_length=100,verbose_name="Site Name")
    site_url=models.CharField(max_length=100,verbose_name="Site URL")
    phone_number=models.CharField(max_length=100,verbose_name="Phone Number",null=True,blank=True)
    address=models.CharField(max_length=100,verbose_name="Address")
    fax_number=models.CharField(max_length=100,verbose_name="Fax Number",null=True,blank=True)
    email=models.CharField(max_length=100,verbose_name="Email",null=True,blank=True)
    about=models.CharField(max_length=100,verbose_name="About")
    copyright=models.CharField(max_length=100,verbose_name="Copyright")
    site_logo=models.ImageField(upload_to='images/settings',verbose_name="Site Logo")
    active=models.BooleanField(verbose_name="Active",default=True)
    twitter = models.URLField(verbose_name='Twitter', blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram', blank=True, null=True)
    linkedin = models.URLField(verbose_name='Linkedin', blank=True, null=True)
    facebook = models.URLField(verbose_name='Facebook', blank=True, null=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'
