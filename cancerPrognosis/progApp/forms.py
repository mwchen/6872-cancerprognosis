from django import forms
from django.db import models
from django.forms import ModelChoiceField
from progApp.models import CancerData

# This model will be used for keeping track of the type of cancer.
class LookUpForm(forms.ModelForm):
	#cancer = forms.ForeignKey(Cancer, help_text="Please enter the type of cancer: ")
	#treatment = forms.ForeignKey(Treatment, null = True, blank = True)
	#stage = forms.ForeignKey(Stage, null = True, blank = True)

	# 0 none 1 boy 2 girl
	gender = forms.IntegerField(initial = 0, help_text="Gender: ")
	age = forms.IntegerField(initial = -1, help_text="Age: ")

	# This will depend on the model needed for the database that has not been created yet.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = CancerData