"""
Definition of models.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from model_utils.fields import StatusField
from model_utils.choices import Choices
#from app.signals import save_csv_data


class Files(models.Model):
    title = models.CharField(max_length=50, null=True, help_text=_("File name"))
    file = models.FileField(upload_to='csv_files/')

    def __unicode__(self):
        return self.title

class Row(models.Model):
    STATUS = Choices(('header', _('header')), ('data', _('data')))

    csv_file = models.ForeignKey(Files)
    row = models.TextField()
    type = StatusField()

    def __unicode__(self):
        return self.row

    @classmethod
    def create(cls, csv_file, row, type='data'):
        row = cls(csv_file=csv_file, row=row, type=type)
        return row