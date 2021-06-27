from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
	class Meta:
		fields = ['username','email','password1','password2']
		model = get_user_model()
		help_texts={
			'username':None,
		}
	def __init__(self,*args,**kwargs):
		super(UserCreateForm,self).__init__(*args,**kwargs)
		self.fields['password2'].label = "Confirm your password "

	def clean_email(self):
		clean_email = super().clean().get('email')
		check_exists = get_user_model().objects.filter(email=clean_email).exists()
		
		if check_exists :
			raise forms.ValidationError("This Email already used by another user ")