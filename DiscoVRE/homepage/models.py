from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
	username = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
	description = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)
	image = models.FileField(null=True, blank=True)

	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')

	def __str__(self):
		return '<Username: {}, ID: {}>'.format(self.username, self.id)

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
	comment = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)

	def approved(self):
		self.approved = True
		self.save()

	def __str__(self):
		return '<Username: {}, ID: {}>'.format(self.user, self.id)
