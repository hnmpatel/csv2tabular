"""
Definition of models.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
#from app.signals import save_csv_data


class Files(models.Model):
    title = models.CharField(max_length=50, null=True, help_text=_("File name"))
    file = models.FileField(upload_to='csv_files/')

    def __unicode__(self):
        return self.title

class Column(models.Model):
    csv_file = models.ForeignKey(Files)
    title = models.CharField(max_length=50, null=True, help_text=_("Gender"))

    def __unicode__(self):
        return self.title

    @classmethod
    def create(cls, csv_file, title):
        column = cls(csv_file=csv_file, title=title)
        return column

class Row(models.Model):
    column = models.ForeignKey(Column)
    title = models.CharField(max_length=50, null=True, help_text=_("Male"))

    def __unicode__(self):
        return self.title

    @classmethod
    def create(cls, column, title):
        row = cls(column=column, title=title)
        return row