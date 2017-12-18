from django.db import models

# Definition of the class person. It will be created one object of this class for each user.
class Person(models.Model):
	username =  models.CharField(max_length=250)
	email =  models.CharField(max_length=250)
	name =  models.CharField(max_length=250, null=True)
	age =  models.IntegerField(null=True)

	def __str__(self):
		return "%s" % (self.username)

# Definition of the class skill. It will be created for each one of the skills and it will have one object of the upper class associated.
class Skill(models.Model):
	person = models.CharField(max_length=250)
	skill = models.CharField(max_length=250)
	number_of_likes =  models.IntegerField(default=0)

	def __str__(self):
		return self.skill