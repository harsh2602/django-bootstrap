from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        #cleaned_data returns a dictionary data structure of the form
        #print self.cleaned_data -->Returns a dictionary
        email = self.cleaned_data.get('email') #Prints only email field

        #if not "@uic.edu" in email:
         #   raise forms.ValidationError("Please use a valid UIC email address")
        #return email

        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if not domain == "uic" or not extension == "edu":
            raise forms.ValidationError("Please use a valid UIC email address")
        #if not extension == "edu":
        #    raise forms.ValidationError("Please use a valid UIC email address")
        return email

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
        #exclude = ['full_name'] --> Use it sparingly

    def clean_email(self):
        #cleaned_data returns a dictionary data structure of the form
        #print self.cleaned_data -->Returns a dictionary
        email = self.cleaned_data.get('email') #Prints only email field

        #if not "@uic.edu" in email:
         #   raise forms.ValidationError("Please use a valid UIC email address")
        #return email

        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if not domain == "uic" or not extension == "edu":
            raise forms.ValidationError("Please use a valid UIC email address")
        #if not extension == "edu":
        #    raise forms.ValidationError("Please use a valid UIC email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        #Write Validation code here
        return full_name