from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView

from portfolio.models import Project
from forms import ContactForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            context['project'] = Project.objects.latest()
        except ObjectDoesNotExist:
            pass

        return context


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        send_mail(
            'Contact from coreymaynard.com',
            self.request.POST.get('message'),
            self.request.POST.get('your_email'),
            [email for name, email in settings.ADMINS]
        )
        return super(ContactView, self).form_valid(form)


class BioView(TemplateView):
    '''My Bio'''
    template_name = 'bio.html'


class ResumeView(TemplateView):
    '''The resume page'''
    template_name = 'resume.html'
