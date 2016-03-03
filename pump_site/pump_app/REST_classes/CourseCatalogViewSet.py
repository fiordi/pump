from django.contrib.auth.models import User
from django.db import models

class CourseCatalog(models.Model):
	id = models.AutoField(primary_key=True)

	name = models.TextField(null=True, blank=False)

	def addCourse(self, Course):
		Course.coursecatalog = self
		Course.save()

	def activateCourse(self, Course):
		Course.open = True
		Course.save()