from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(label="Your Name")
    your_email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea)
