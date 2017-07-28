from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Kill_PureText(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return str(self.id)