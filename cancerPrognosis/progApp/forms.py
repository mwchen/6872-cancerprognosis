from django.db import models
from django import forms
from progApp.models import Patient

# This model will be used for keeping track of the type of cancer.
class LookUpForm(forms.ModelForm):
	typeCancer = forms.CharField(max_length=128, help_text="Please enter the type of cancer: ")
	ageRange = forms.IntegerField(help_text="Please enter the age of the patient: ")

	# This will depend on the model needed for the database that has not been created yet.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Patient