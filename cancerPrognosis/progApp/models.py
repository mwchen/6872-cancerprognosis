from django.db import models

class Patient(models.Model):
	typeCancer = models.CharField(max_length=128)
	ageRange = models.IntegerField()