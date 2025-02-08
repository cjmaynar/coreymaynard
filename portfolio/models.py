from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    begun = models.DateField()
    completed = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField()
    short_lead = models.CharField(max_length=200)
    languages = models.ManyToManyField('Language', related_name="used_in")
    images = models.ManyToManyField('core.image', related_name='projects')
    primary = models.ForeignKey('core.image', related_name='primary', on_delete=models.CASCADE)

    def save(self):
        from django.template.defaultfilters import slugify
        self.slug = slugify(self.title)
        super(Project, self).save()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-completed',)
        get_latest_by = 'completed'


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
