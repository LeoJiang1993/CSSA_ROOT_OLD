from django import forms
from django.forms import widgets


class NewsEdit(forms.Form):
    id = forms.IntegerField()
    title = forms.CharField(max_length=20)
    author = forms.CharField(max_length=20)
    content = forms.CharField(max_length=2000)
    banner = forms.ImageField(required=False)
    status = forms.IntegerField()
    topic = forms.IntegerField()
    activity = forms.IntegerField(required=False)
    comment = forms.BooleanField(
        widget=widgets.CheckboxInput(), label='comment', required=False
    )
