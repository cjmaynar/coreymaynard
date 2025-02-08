from django.views.generic import ListView, DetailView

from .models import Project


class PortfolioList(ListView):
    template_name = 'portfolio/index.html'
    model = Project


class PortfolioDetail(DetailView):
    template_name = 'portfolio/detail.html'
    model = Project
