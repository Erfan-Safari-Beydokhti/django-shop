from django.contrib import admin
from .models import SiteSettings,FooterLinkBox,FooterLink
# Register your models here.

admin.site.register(SiteSettings)
admin.site.register(FooterLinkBox)
admin.site.register(FooterLink)
