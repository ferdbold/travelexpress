from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50, widget=forms.PasswordInput)
	password_validation = forms.CharField(label='Password (again)', max_length=50, widget=forms.PasswordInput)
	phone_number = forms.CharField(max_length=10)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()

		username = cleaned_data.get('username')
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
		password_validation = cleaned_data.get('password_validation')

		if username:
			try:
				existing_username = User.objects.get(username=username)
				self.add_error('username', 'This username is not available')
			except User.DoesNotExist:
				existing_username = None

		if email:
			try:
				existing_email = User.objects.get(email=email)
				self.add_error('email', 'This email address is not available')
			except User.DoesNotExist:
				existing_email = None

		if password and password_validation and (password != password_validation):
			msg = 'The passwords don\'t match'
			self.add_error('password', msg)
			self.add_error('password_validation', msg)

		return cleaned_data
