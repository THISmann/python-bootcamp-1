from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Write your name here'
        })
    )
    email = forms.EmailField(
        label="Type your email",
        help_text='Must contain al least 8 characters',
        error_messages={'required': 'Please enter a valid email address'})
    comment = forms.CharField(widget=forms.Textarea)
