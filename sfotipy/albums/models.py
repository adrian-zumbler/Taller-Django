from django.db import models

class Albums(models.Model):
    name = models.CharField(max_length=255)
    cover = models.FileField(upload_to='songs/')
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.name
