from django import forms

class NewQuoteForm(forms.Form):
    quote = forms.CharField()
    speaker = forms.CharField(max_length="100")
