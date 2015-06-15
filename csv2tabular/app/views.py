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
    data = {}

    file = Files.objects.get(id=int(fid))
    columns = Row.objects.get(csv_file=file, type='header').row.split(',')
    c1, c2 = 0, 0

    for idx, col in enumerate(columns):
        if col == col1:
            c1 = idx
            continue
        if col == col2:
            c2 = idx

    c_list = [];
    r_list = [];
    result = {};
    temp = {}
    rows = Row.objects.filter(csv_file=file, type='data')
    for idx, row in enumerate(rows):
        cols = row.row.split(',')
        if not temp.has_key(cols[c2]):
            c_list.append(cols[c2])
            temp[cols[c2]] = []
            
        if result.has_key(cols[c1]):
            result[cols[c1]].append(cols[c2])
        else:
            r_list.append(cols[c1])
            result[cols[c1]] = []
            result[cols[c1]].append(cols[c2])

    count = 0;
    for key in result.keys():
        data[key] = {}
        for c in c_list:
            count = 0;
            for ele in result[key]:
                if ele == c:
                    count += 1;
            data[str(key)][str(c)] = count

    return render(
        request,
        'app/show_tabular_data.html',
        context_instance = RequestContext(request,
        {
            'file': file,
            'columns': columns,
            'header': c_list,
            'rows': r_list,
            'data' : data,
        })
    )