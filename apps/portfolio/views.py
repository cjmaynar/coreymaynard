from django.shortcuts import render_to_response
from django.template  import RequestContext
from django.http      import HttpResponseNotFound

from .models import Project


def portfolio_index(request):
    '''Render the main page of the portfolio'''
    try:
        projects = Project.objects.all()
    except:
        latest = None

    return render_to_response("portfolio/index.html", \
            context_instance=RequestContext(request, vars()))


def portfolio_detail(request, slug):
    '''Render an individual page of the portfolio'''
    project = Project.objects.get(slug=slug)

    return render_to_response("portfolio/detail.html", \
            context_instance=RequestContext(request, vars()))
