from django.db import models

class Person(models.Model):
	name =  models.CharField(max_length=250)
	age =  models.CharField(max_length=250)
	sex =  models.CharField(max_length=250)
	#photo =  models.CharField(max_length=250)

	def __str__(self):
		return "%s %s" % (self.name, self.age)


class Skill(models.Model):

	skill = models.CharField(max_length=250)
	person = models.ForeignKey(Person)

	def __str__(self):
		return self.skill