from django.db import models
from django import forms


class EmailSending(models.Model):
    email = models.EmailField()
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email


class EmailForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email Address '}))
    label = {
        'email': 'Email Address',
    }

    class Meta:
        fields = ('email',)
        model = EmailSending
