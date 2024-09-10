from django import forms

class createForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Bootstrap class for styling
            'style': 'width: 100%;'   # Ensure full width within parent container
        })
    )
    age = forms.CharField(
        max_length=200,
        label="Age",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Bootstrap class for styling
            'style': 'width: 100%;'   # Ensure full width within parent container
        })
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',  # Bootstrap class for styling
        }),
        label="Date"
    )
    password = forms.CharField(
        max_length=200,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'  # Bootstrap class for styling
        })
    )
    check = forms.BooleanField(
        label="Check",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'  # Bootstrap class for styling checkboxes
        })
    )
