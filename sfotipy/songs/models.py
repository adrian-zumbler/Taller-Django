from django.db import models

from albums.models import Albums

class Song(models.Model):
    name = models.CharField(max_length=255)
    filename = models.FileField(upload_to='canciones/')
    album = models.ForeignKey(Albums)

    def __unicode__(self,):
        return self.name
