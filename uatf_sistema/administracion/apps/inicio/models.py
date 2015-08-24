from django.db import models

# Create your models here.

class Carrera(models.Model):
	Nombre_Carrera = models.CharField(max_length=60)

	def __unicode__(self):
		return self.Nombre_Carrera
