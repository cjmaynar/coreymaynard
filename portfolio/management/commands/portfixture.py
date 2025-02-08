import datetime

from django.core.management.base import BaseCommand
from portfolio.models import Project, Language


class Command(BaseCommand):
    def run_from_argv(self, *args):

        languages = (
            'PHP',
            'MySQL',
            '(X)HTML',
            'CSS',
            'Python/Django',
            'JavaScript/jQuery',
        )

        # Build Technologies
        print "Adding languages..."
        for lang in languages:
            l = Language()
            l.name = lang
            l.save()

        today = datetime.date.today()
        start = today - datetime.timedelta(weeks=15)

        print "Adding projects..."
        for i in range(4):
            if i == 0:
                i = 1

            languages = Language.objects.get(pk=i)

            p = Project()
            p.begun = start
            p.completed = today
            p.title = "Project Number %s" % (i,)
            p.slug = "project-%s" % (i,)
            p.client = "Myself"
            p.description = "I did stuff on this project"
            p.save()
            p.languages.add(languages)
            p.save()
