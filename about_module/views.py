from django.views.generic import ListView

from about_module.models import About, TeamMember, ClientsFeedback

from django.views.generic import TemplateView
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about_module/about.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['about']=About.objects.first()
        context['team_members']=TeamMember.objects.all()
        context['feedbacks']=ClientsFeedback.objects.all()
        return context


