from django import forms
from django.db import models
from django.forms import ModelChoiceField
from progApp.models import Cancer, CancerData, Stage, Treatment, LookUpData

# This model will be used for keeping track of the type of cancer.
class LookUpForm(forms.ModelForm):
	# This will depend on the model needed for the database that has not been created yet.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = LookUpData
		
