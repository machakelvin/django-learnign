from django import forms

class createForm(forms.Form):
    name = forms.CharField(max_length=200, label="Name")
    age = forms.CharField(max_length=200, label="Age")
    date = forms.DateField()
    password = forms.CharField(max_length=200, label="Password")
    check = forms.BooleanField()