from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
	name = models.CharField(max_length=100, blank=True)
	url = models.URLField('URL', unique=False, blank=True)
	media = models.FileField(upload_to="Uploads/projects", blank=False,
                                 null=False, help_text='Cover image for projects.')
	owner = models.ForeignKey(User, on_delete=models.CASCADE,)

	class Meta:
		ordering = ['name']
		verbose_name_plural = "Projects"

	def __str__(self):
		return self.name