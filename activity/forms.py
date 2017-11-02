from django import forms


class EditActivity(forms.Form):
    id = forms.IntegerField(required=False)
    description = forms.CharField(max_length=100)
    time = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S',
                                              '%Y-%m-%dT%H:%M'])
    capacity = forms.IntegerField()
    status = forms.IntegerField()
