from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='your email')
    comment = forms.CharField()