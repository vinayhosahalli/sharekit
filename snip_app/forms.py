from django import forms
from .models import Snip
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User


class snipForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model = Snip
        widgets = {'author': forms.HiddenInput()}
        fields = ('author', 'text', 'title', 'is_encrypted')
        labels = {'title': 'Snippet Title', 'text': 'New Snippet', 'is_encrypted': 'Encrypt'}


class searchForm(forms.Form):
    helper = FormHelper()
    search = forms.CharField(max_length=100, widget=forms.TextInput
    (attrs={'class': 'is-small input is-info', 'placeholder': 'Search Text Here'}))
