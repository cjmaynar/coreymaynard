from django.db import models


class ImageManager(models.Manager):
    @property
    def screenshot(self):
        return self.filter(use=1)

    @property
    def code(self):
        return self.filter(use=2)


class Image(models.Model):
    '''Every post should have an image to go with it'''
    USES = (
        (0, ''),
        (1, 'Screenshot'),
        (2, 'Code')
    )

    title = models.CharField(max_length=128)
    fullsize = models.FileField(upload_to='uploads')
    small = models.FileField(upload_to='uploads/small', editable=False)
    source = models.CharField(max_length=256, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)
    use = models.PositiveSmallIntegerField(choices=USES, default=USES[0][0])

    objects = ImageManager()

    def save(self):
        '''On save, create a downsized image to use as a preview.'''
        try:
            import Image as img
            import settings
            filename = self.fullsize
            image = img.open(filename)

            height, width = image.size

            while height > 600:
                height = height / 2
                width = width / 2

            image.thumbnail((height, width))
            image.save('%s/files/uploads/small/%s' % \
                    (settings.PROJECT_ROOT, self.fullsize), 'JPEG', quality=80)

            self.small = 'uploads/small/%s' % (filename)
        except:
            print "error on save stuff"

        super(Image, self).save()

    def __unicode__(self):
        return self.title
