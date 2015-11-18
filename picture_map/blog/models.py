from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	autor = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.titulo