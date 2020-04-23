from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
# Create your models here.
class uuprofile(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length=100, default='')
	country = models.CharField(max_length=100, default='')
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = uuprofile.objects.create(usuario=kwargs['instance'],email=kwargs['instance'].email)
post_save.connect(create_profile,sender=User)

	

class dadosmodels(models.Model):
	dictStringResult=models.TextField(default='')
	paymentMethod = models.CharField(max_length=100,default='')
	yearsTopay = models.FloatField(default=0)
	entry = models.FloatField(default=0)
	usuario = models.CharField(max_length=100,default='')
	energyconsume = models.FloatField(default=0)
	radiation1 = models.CharField(max_length=100, default='')
	radiation2 = models.FloatField(default=0)
	radiation3 = models.FloatField(default=0)
	pricekwh= models.FloatField(default=0)
	economy= models.FloatField(default=0)
	painelpower= models.FloatField(default=0)
	panelprice1= models.CharField(max_length=100, default='')
	panelprice2= models.FloatField(default=0)
	panelprice3= models.FloatField(default=0)
	priceinverters1= models.CharField(max_length=100, default='')
	priceinverters2= models.FloatField(default=0)
	priceinverters3= models.FloatField(default=0)
	pricestringbox= models.FloatField(default=0)
	priceproject= models.FloatField(default=0)
	pricewiring= models.FloatField(default=0)
	pricess= models.FloatField(default=0)
	pricelabor= models.FloatField(default=0)
	maintenance= models.FloatField(default=0)
	inflation= models.FloatField(default=0)
	ccp1= models.CharField(max_length=100, default='')
	ccp2= models.FloatField(default=0)
	ccp3= models.FloatField(default=0)
	cct1= models.CharField(max_length=100, default='')
	cct2= models.FloatField(default=0)
	cct3= models.FloatField(default=0)
	pccp= models.FloatField(default=0)
	pcct= models.FloatField(default=0)
	plifespan1= models.CharField(max_length=100, default='')
	plifespan2= models.FloatField(default=0)
	plifespan3= models.FloatField(default=0)
	plifespan4= models.FloatField(default=0)
	plifespan5= models.FloatField(default=0)
	plifespan6= models.FloatField(default=0)
	plifespan7= models.FloatField(default=0)
	ilifespan1= models.CharField(max_length=100, default='')
	ilifespan2= models.FloatField(default=0)
	ilifespan3= models.FloatField(default=0)
	ilifespan4= models.FloatField(default=0)
	ilifespan5= models.FloatField(default=0)
	ilifespan6= models.FloatField(default=0)
	ilifespan7= models.FloatField(default=0)
	preduction= models.FloatField(default=0)
	projeto= models.CharField(max_length=100, default='')
	maintenance1= models.CharField(max_length=100, default='')
	maintenance2= models.FloatField(default=0)
	maintenance3= models.FloatField(default=0)
	energy_production_tax=models.FloatField(default=0)
	depreciation_years_inverters=models.FloatField(default=0)
	depreciation_years_painels =models.FloatField(default=0)
	person_or_business_or_sellenergy= models.CharField(max_length=100, default='')
	incometax=models.FloatField(default=0)
	sim_year=models.FloatField(default=0)
	
	
class testmodels(models.Model):
	test1 = models.CharField(max_length=100,default='')



	

