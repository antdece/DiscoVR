from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	description = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Username: {}, ID: {}>'.format(self.username, self.id)