"""
Definition of models.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Files(models.Model):
    title = models.CharField(max_length=50, null=True, help_text=_("File name"))
    file = models.FileField(upload_to='csv_files/')

    def __unicode__(self):
        return self.title