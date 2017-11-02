from django import forms


class ModifyAccount(forms.Form):
    nick_name = forms.CharField(max_length=20)
    photo = forms.ImageField(required=False)
    last_name = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)


class CreateAccount(forms.Form):
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    nick_name = forms.CharField(max_length=20)
    photo = forms.ImageField(required=False)
    email = forms.EmailField()
    last_name = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
