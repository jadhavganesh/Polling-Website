from django import forms
from .models import Snippet

class ContactForm(forms.Form):
	name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	email = forms.EmailField(label='Email')    
	mobile = forms.CharField(label='Mobile')
	
	
	
	
		
		
	
	
class SnippetForm(forms.ModelForm):

	class Meta:
		model = Snippet
		fields = ('name','last_name','email','mobile')
