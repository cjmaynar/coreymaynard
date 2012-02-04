from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from settings import USER_NAME
from blog.models import Post, Comment

class Command(BaseCommand):
    def run_from_argv(self, *args):
        print 'Installing posts...'
        
        user = User.objects.get(username=USER_NAME)
        
        for i in range(0,10):
            post = Post(
                slug = 'post_url'+str(i),
                title = 'Test Post',
                author = user,
                status = True,
                body = 'Test Content',
            )
            post.save()

            comment = Comment(
                post = post,
                author = 'John Doe',
                author_url = 'http://www.johndoe.com',
                author_email = 'john@doe.com',
                comment = 'Generic comment %s' % (i),
            )
            comment.save()
        print 'Content added'
