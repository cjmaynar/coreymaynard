from django.shortcuts import render_to_response
from django.template  import RequestContext
from blog.models      import Post
from forms            import ContactForm


def index(request):
    '''The home page of the site'''
    from portfolio.models import Project
    project = Project.objects.latest()
    return render_to_response("index.html", context_instance=RequestContext(request, vars()))


def contact(request):
    '''Get in touch with me'''
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            print request.POST

            from django.core.mail import send_mail

            send_mail('Contact from coreymaynard.com', request.POST.get('message'), request.POST.get('your_email'), ['me@coreymaynard.com'])
            sent = True
    else:
        form = ContactForm()
    return render_to_response("contact.html", context_instance=RequestContext(request, vars()))


def bio(request):
    '''My Bio'''
    is_bio = True

    return render_to_response("bio.html", context_instance=RequestContext(request, vars()))


def resume(request):
    '''The resume page'''
    return render_to_response("resume.html", context_instance=RequestContext(request, vars()))


def search(request):
    '''Search for a blog post.'''
    from django.db.models import Q
    qstring = request.GET.get('q', '').strip()

    if qstring:
        searched = True
        results  = Post.objects.filter(
            Q(title__icontains=qstring) | Q(body__icontains=qstring)
        )
    else:
        searched = False

    return render_to_response("search.html", context_instance=RequestContext(request, vars()))
