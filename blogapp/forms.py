from django import forms
from django.contrib.auth.models import User
from blogapp.models import blogtable

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')
        widgets={'password':forms.PasswordInput()}

class postform(forms.ModelForm):
    class Meta:
        model=blogtable
        fields=('Title','Description','Image')
        widgets={'Description':forms.Textarea(attrs={'rows':6,'cols':35})}
