"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import UploadForm
from django.shortcuts import HttpResponseRedirect
from app.models import Files

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
