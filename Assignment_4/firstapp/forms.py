from django import forms

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Song List',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'Please enter song:'
            }))
