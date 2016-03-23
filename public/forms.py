from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
	
    def clean(self):
    	password1 = self.cleaned_data.get('password')
    	password2 = self.cleaned_data.get('password_validation')

    	if not password2 :
    		raide ValidationError("You have to validate your password")

        if password1 != password2:
            raise ValidationError("Email addresses must match.")

        return self.cleaned_data