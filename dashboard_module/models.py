from django.db import models

from account_module.models import User


# Create your models here.
class AddressBook(models.Model):
    COUNTRY_CHOICES = [
        ('us',"United States"),
        ('uk',"United Kingdom"),
        ('uae',"United Arab Emirates"),
    ]
    STATE_CHOICES = [
        ("ny", "New York"),
        ("al", "Alabama"),
        ("ak", "Alaska"),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='addresses')
    first_name = models.CharField(max_length=50,verbose_name="First Name")
    last_name = models.CharField(max_length=50,verbose_name="Last Name")
    phone_number = models.CharField(max_length=50,verbose_name="Phone Number")
    street_address = models.CharField(max_length=50,verbose_name="Street Address")
    country = models.CharField(max_length=50,verbose_name="Country",choices=COUNTRY_CHOICES)
    state = models.CharField(max_length=50,verbose_name="State",choices=STATE_CHOICES)
    city = models.CharField(max_length=50,verbose_name="City")
    zip_code = models.CharField(max_length=50,verbose_name="Zip Code")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Address Book'
        verbose_name = 'Address Book'