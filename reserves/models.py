import datetime
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.
class Sala(models.Model):
	text_sala = models.CharField(max_length=200)
	aforo = models.IntegerField(default=1)
	def __str__(self):
		return self.text_sala

class Material(models.Model):
	sala_f = models.ForeignKey(Sala, on_delete=models.CASCADE)
	text_material = models.CharField(max_length=200)
	
	def __str__(self):
		return self.text_material

class Reserva(models.Model):
	user_f = models.ForeignKey(User, on_delete=models.CASCADE)
	material = models.ManyToManyField(Material)
	reserva_date = models.DateTimeField('Data reserva')


	def show_material(self):
		s=""
		for mat in self.material.all():
			s+=mat.text_material+","
		return s
	
	def was_published_recently(self):
		return self.reserva_date >= timezone.now() - datetime.timedelta(days=1)
