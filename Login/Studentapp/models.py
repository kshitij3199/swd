from django.db import models
import datetime

class Studentclass(models.Model):
	namestudent = models.CharField(max_length=200)
	departure_date = models.DateField(default=datetime.date.today)
	arrival_date = models.DateField(default=datetime.date.today)
	approval = models.BooleanField(default=False)
	days = models.IntegerField(default=0)
	
	