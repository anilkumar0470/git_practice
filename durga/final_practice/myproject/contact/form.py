from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    comments = forms.CharField()
    number = forms.IntegerField()

