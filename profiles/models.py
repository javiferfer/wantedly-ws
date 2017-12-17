from django.db import models

class Person(models.Model):
	username =  models.CharField(max_length=250)
	email =  models.CharField(max_length=250)
	name =  models.CharField(max_length=250, null=True)
	age =  models.IntegerField(null=True)

	def __str__(self):
		return "%s" % (self.username)


class Skill(models.Model):

	# person = models.ForeignKey(Person)
	person = models.CharField(max_length=250)
	skill = models.CharField(max_length=250)
	number_of_likes =  models.IntegerField(default=0)

	def __str__(self):
		return self.skill