from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    phone = models.CharField(max_length=255,null=True)
    user = models.OneToOneField(User)
