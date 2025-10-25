from django.contrib import admin

# Register your models here.

from .models import About,TeamMember,ClientsFeedback

admin.site.register(About)
admin.site.register(TeamMember)
admin.site.register(ClientsFeedback)