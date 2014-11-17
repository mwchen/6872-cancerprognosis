from django import forms
from django.db import models
from django.forms import ModelChoiceField
from progApp.models import Cancer, CancerData, Stage, Treatment

# This model will be used for keeping track of the type of cancer.
class LookUpForm(forms.ModelForm):
	# TODO: Need to fix the message to get rid of 
	# "Hold down "Control", or "Command" on a Mac, to select more than one. "
	#cancer = forms.ModelMultipleChoiceField(queryset=Cancer.objects.all(), \
	#	help_text="Type of cancer: ")
	#stage = forms.ModelMultipleChoiceField(queryset=Stage.objects.all(), \
	#	help_text="Stage: ")


	# 0 none 1 boy 2 girl
	gender = forms.IntegerField(initial = 0)
	age = forms.IntegerField(initial = -1)

	# This will depend on the model needed for the database that has not been created yet.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = CancerData
