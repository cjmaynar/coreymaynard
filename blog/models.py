from django.db import models


class Post(models.Model):
    '''This runs all the blog posts.'''
    slug = models.SlugField(unique_for_date='date', editable=False)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    published = models.BooleanField(default=False)
    body = models.TextField()
    lead = models.TextField()
    allow_comments = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', related_name="posts", blank=True)
    image = models.ForeignKey('core.Image', related_name='post', blank=True, null=True, on_delete=models.CASCADE)

    def save(self):
        from django.template.defaultfilters import slugify
        if not self.date:
            from datetime import datetime
            self.date = datetime.now()

        self.slug = slugify(self.title)
        super(Post, self).save()

    def get_prev(self):
        return self.get_previous_by_publish(published=True)

    def get_next(self):
        return self.get_next_by_publish(published=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-date',)
        get_latest_by = 'date'


class CommentManager(models.Manager):
    @property
    def approved_only(self):
        return self.get_query_set().exclude(approved=False)


class Comment(models.Model):
    '''Have something to say about a post? Say it here'''
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    author_url = models.URLField(blank=True, null=True)
    author_email = models.EmailField(blank=True, null=True)
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    admin_comment = models.BooleanField(default=False)

    objects = CommentManager()

    def __unicode__(self):
        return self.author + " " + str(self.date)


class Category(models.Model):
    '''What category does a post belong in? Pick it here'''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
