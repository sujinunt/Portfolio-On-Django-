from django import forms
class TestForm(forms.Form):
    Email = forms.EmailField()
    Subject = forms.CharField(max_length=255)
    Message = forms.CharField(widget=forms.Textarea)