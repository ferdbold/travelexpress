from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(label='Nom d\'utilisateur', max_length=50)
	password = forms.CharField(label='Mot de passe', max_length=50, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='Prénom', max_length=100)
	last_name = forms.CharField(label='Nom', max_length=100)
	email = forms.EmailField(label='Courriel', max_length=100)
	username = forms.CharField(label='Nom d\'utilisateur', max_length=50)
	password = forms.CharField(label='Mot de passe', max_length=50, widget=forms.PasswordInput)
	password_validation = forms.CharField(label='Mot de passe (vérification)', max_length=50, widget=forms.PasswordInput)
	phone_number = forms.CharField(label='Numéro de téléphone', max_length=10)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()

		username = cleaned_data.get('username')
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
		password_validation = cleaned_data.get('password_validation')

		if username:
			try:
				existing_username = User.objects.get(username=username)
				self.add_error('username', 'Cet utilisateur existe déjà')
			except User.DoesNotExist:
				existing_username = None

		if email:
			try:
				existing_email = User.objects.get(email=email)
				self.add_error('email', 'Cette adresse courriel est déjà utilisée')
			except User.DoesNotExist:
				existing_email = None

		if password and password_validation and (password != password_validation):
			msg = 'Les mots de passe ne sont pas identiques'
			self.add_error('password', msg)
			self.add_error('password_validation', msg)

		return cleaned_data
