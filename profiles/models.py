from django.db import models

class Javi(models.Model):
	skill =  models.CharField(max_length=250)

	def __str__(self):
		return self.skill

class Ruben(models.Model):
	skill =  models.CharField(max_length=250)

	def __str__(self):
		return self.skill