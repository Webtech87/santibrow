from django import forms
from django.db import models
class ContactForm(forms.Form):
	class SubjectOptions(models.TextChoices):
		select = "Select", "Select"
		option1 = "option1", "option1"
		option2 = "option2", "option2"
		option3 = "option3", "option3"
		option4 = "option4", "option4"
		option5 = "option5", "option5"
		
	name = forms.CharField(max_length=100)
	subject = forms.ChoiceField(choice=SubjectOptions, max_length=25, initial="Selsect")
	email = forms.EmailField()
	tel = forms.CharField(max_length=20)
	message = forms.CharField(widget=forms.Textarea)
