from django.shortcuts import render
from django.views.generic import TemplateView

from about_module.models import About, TeamMember, ClientsFeedback


# Create your views here.


class AboutView(TemplateView):
    model=About
    template_name = 'about_module/about.html'
    context_object_name = 'about'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['team_members']=TeamMember.objects.all()
        context['feedbacks']=ClientsFeedback.objects.all()
        return context


