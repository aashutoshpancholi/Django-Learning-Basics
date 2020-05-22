from django import forms

class feedbackform(forms.Form):
    email = forms.CharField(label='E Mail', min_length=1, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Subject', min_length=1, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', min_length=1, widget=forms.Textarea(attrs={'class': 'form-control'}))