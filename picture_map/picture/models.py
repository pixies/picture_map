from django.db import models
from django.conf import settings

# Create your models here.
class Picture(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.CharField(max_length=200)
	latitude = models.CharField(max_length=20)
	longitude = models.CharField(max_length=20)
	dono = models.ForeignKey(settings.AUTH_USER_MODEL)
	arquivo = models.FileField(upload_to='images/%Y/%m/%d')

	def __unicode__(self):
		return self.nome