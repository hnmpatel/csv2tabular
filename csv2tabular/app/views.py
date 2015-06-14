"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import UploadForm
from django.shortcuts import HttpResponseRedirect
from app.models import Files, Row

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    files = Files.objects.all()
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'files': files,
        })
    )

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadForm()
    return render(
        request,
        'app/upload.html',
        context_instance = RequestContext(request,
        {
            'form': form
        })
    )

def view_data(request, id):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    file = Files.objects.get(id=id)
    return render(
        request,
        'app/show_data.html',
        context_instance = RequestContext(request,
        {
            'file': file,
        })
    )

def view_db_data(request, id):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    file = Files.objects.get(id=id)
    columns = Row.objects.get(csv_file=file, type='header').row.split(',')
    return render(
        request,
        'app/show_db_data.html',
        context_instance = RequestContext(request,
        {
            'file': file,
            'columns': columns,
        })
    )

def tabular_data(request, fid, col1, col2):
    file = Files.objects.get(id=int(fid))
    columns = Row.objects.get(csv_file=file, type='header').row.split(',')
    idx1, idx2 = 0, 0

    for idx, col in enumerate(columns):
        if col == col1:
            idx1 = idx
            continue
        if col == col2:
            idx2 = idx

    x = set()
    y = set()
    rows = Row.objects.filter(csv_file=file, type='data')
    for row in rows:
        cells = row.row.split(',')
        t = tuple(cells[idx1], cells[idx2])
        x.add(cells[idx1])
        y.add(cells[idx2])
        if cells[idx1] in x:
            pass
        else:
            pass

        print cells[idx2]

    data = list()
    result = dict()

    return render(
        request,
        'app/show_tabular_data.html',
        context_instance = RequestContext(request,
        {
            'file': file,
            'columns': columns,
        })
    )