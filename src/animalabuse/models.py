from django.db import models

# Create your models here.
class animalabuse(models.Model):
	name = models.CharField(max_length = 120)
	DOB = models.TextField(blank = True, null = True)
	Age = models.DecimalField(decimal_places = 0, max_digits = 3)
	county = models.CharField(blank = True, null = True, max_length = 120)
	Address = models.TextField(blank = True, null = True)
	Offense = models.TextField(blank = True, null = True)
	convictiondate = models.DateField() 
	expirationdate = models.DateField(null = True)
	image = models.URLField(null = True)
