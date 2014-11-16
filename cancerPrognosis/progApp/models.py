from django.db import models

# Create your models here.
class Cancer(models.Model):
	type = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000)
	
class Treatment(models.Model):
	cancer = models.ForeignKey(Cancer)
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000)

class Stage(models.Model):
	cancer = models.ForeignKey(Cancer)
	name = models.IntegerField()
	description = models.CharField(max_length = 1000)

class CancerData(models.Model):
	cancer = models.ForeignKey(Cancer)
	treatment = models.ForeignKey(Treatment, null = True, blank = True)
	stage = models.ForeignKey(Stage, null = True, blank = True)
	# 0 none 1 boy 2 girl
	gender = models.IntegerField(default = 0)
	age = models.IntegerField(default = -1)
	
class quickCancerLookup(models.Model):
	name = models.CharField(max_length = 1000)
	data = models.CharField(max_length = 1000)

class trustedDoctors(models.Model):
	pin = models.CharField(max_length = 500)
	name = models.CharField(max_length = 500)

