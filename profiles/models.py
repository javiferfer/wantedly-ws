from django.db import models

class Person(models.Model):
	username =  models.CharField(max_length=250)
	email =  models.CharField(max_length=250)
	# age =  models.IntegerField()
	# sex =  models.CharField(max_length=250)
	#photo =  models.CharField(max_length=250)

	def __str__(self):
		return "%s" % (self.username)


class Skill(models.Model):

	skill = models.CharField(max_length=250)
	person = models.ForeignKey(Person)
	category =  models.CharField(max_length=250)

	def __str__(self):
		return self.skill