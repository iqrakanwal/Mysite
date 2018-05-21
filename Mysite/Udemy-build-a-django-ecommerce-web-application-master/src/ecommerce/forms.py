from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    title = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "title"
                    }
                    )
            )
    slug = forms.SlugField(widget=forms.SlugField())
    Description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "description"
            }
        )
    )
    price= forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"price",
        "class":"form_control"
    }))


    image= forms.ImageField()



    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email















