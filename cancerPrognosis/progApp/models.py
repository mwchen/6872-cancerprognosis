from django.db import models

class Cancer(models.Model):
	type = models.CharField(max_length = 100, unique = True)
	description = models.CharField(max_length = 1000)
	
	def __str__(self):
		return self.type

class Treatment(models.Model):
	cancer = models.ForeignKey(Cancer)
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000)
	quality_of_life = models.PositiveIntegerField(null = True, blank = True)
	cost = models.PositiveIntegerField(null = True, blank = True)
	unique_together = (('cancer','name'),)
	
	def __str__(self):
		return self.name

class Stage(models.Model):
	cancer = models.ForeignKey(Cancer)
	name = models.PositiveIntegerField()
	description = models.CharField(max_length = 1000)
	unique_together = (('cancer','name'),)
	
	def __str__(self):
		return self.name

class Gender(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

class CancerData(models.Model):
	cancer = models.ForeignKey(Cancer)
	treatment = models.ForeignKey(Treatment, null = True, blank = True)
	stage = models.PositiveIntegerField(null = True, blank = True)
	gender = models.ForeignKey(Gender, null = True, blank = True)
	age = models.PositiveIntegerField(null = True, blank = True)
	years_lived = models.PositiveIntegerField(default = 0)

class LookUpData(models.Model):
	cancer = models.ForeignKey(Cancer)
	stage = models.PositiveIntegerField(null = True, blank = True)
	age = models.PositiveIntegerField(null = True, blank = True)
	gender = models.ForeignKey(Gender, null = True, blank = True)
	
class quickCancerLookup(models.Model):
	name = models.CharField(max_length = 1000)
	cancer = models.ForeignKey(Cancer, null = True, blank = True)
	data = models.CharField(max_length = 1000)

class trustedDoctors(models.Model):
	pin = models.CharField(max_length = 500)
	name = models.CharField(max_length = 500)


	