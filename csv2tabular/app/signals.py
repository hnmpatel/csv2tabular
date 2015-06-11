from django.db.models.signals import post_save
from app.models import Files, Column, Row

import csv

def save_csv_data(sender, instance, **kwargs):
    with open (instance.file.url, 'r') as f:
        csv_data = csv.reader(f)
        col = False
        columns = []
        for column in csv_data:
            if not col:
                for c in column:
                    columns.append(Column.create(instance, c))
                for c in columns:
                    c.save()
                col = True
                continue
            for i, c in enumerate(column):
                r = Row.create(columns[i], c)
                r.save()

post_save.connect(save_csv_data, sender=Files)