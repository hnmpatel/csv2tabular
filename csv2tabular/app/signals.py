from django.db.models.signals import post_save
from app.models import Files, Row

import csv

def save_csv_data(sender, instance, **kwargs):
    with open (instance.file.url, 'r') as f:
        csv_data = csv.reader(f)
        col = False
        columns = []
        for column in csv_data:
            if not col:
                header = Row.create(instance, str(','.join(column)), type='header')
                header.save()
                col = True
                continue
            r = Row.create(instance, str(','.join(column)))
            r.save()

post_save.connect(save_csv_data, sender=Files)