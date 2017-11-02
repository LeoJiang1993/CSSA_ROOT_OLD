from django import forms


class NewComment(forms.Form):
    news_id = forms.IntegerField()
    content = forms.CharField(max_length=200)
