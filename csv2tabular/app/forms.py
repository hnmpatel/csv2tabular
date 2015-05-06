"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Files

class UploadForm(forms.ModelForm):
    """Upload form to upload file."""
    class Meta:
        model = Files
        fields = ['title', 'file']