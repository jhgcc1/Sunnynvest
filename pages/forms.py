from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ValidationError
from django.shortcuts import render , redirect

class changepass(PasswordChangeForm):	
    
	class Meta:
		model = User
		fields = ('old_password',
		'new_password2',
		'new_password1')
		#'extra_field')
		
	def __init__(self, *args, **kwargs):
		super(changepass, self).__init__(*args, **kwargs)
		for x in self.fields:
			self.fields[x].widget.attrs.update({'class' : 'form-control'})
		#self.fields['old_password'].widget.attrs.update({'class' : 'form-control'})
		#self.fields['extra_field'].label = "Country:"
		#for fieldname in ['username', 'password1', 'password2']:
			#ajaja=1
			#self.fields[fieldname].help_text =
 		
	def save(self, commit=True,*args, **kwargs):
		user = super(changepass, self).save(commit=False)
		
		#user.extra_field = request.POST.get('pais')
		
	
		
		if commit:
			user.save()	
			
			return user



paises=['brasil','argentina','jjjj']

class registrationform(UserCreationForm):	
    
	class Meta:
		model = User
		fields = ('username',
		'first_name',
		'last_name',
		'email',
		'password1',
		'password2')
		#'extra_field')
		
	def __init__(self, *args, **kwargs):
		super(registrationform, self).__init__(*args, **kwargs)
		#self.fields['extra_field'].label = "Country:"
		for fieldname in ['username', 'password1', 'password2']:
			ajaja=1
			#self.fields[fieldname].help_text =
		for x in self.fields:
			self.fields[x].widget.attrs.update({'class' : 'form-control'})


	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise ValidationError("This email address is already in use. Please supply a different email address.")
		return email


	def save(self, commit=True,*args, **kwargs):
		user = super(registrationform, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']	
		username= self.cleaned_data['username']
		#user.extra_field = request.POST.get('pais')
		
	

		if commit:
			user.save()	
			
			return user
class dadosform(forms.Form):
	clientShare=forms.CharField()
	dictStringResult=forms.CharField()
	usuario= forms.CharField()
	paymentMethod = forms.CharField()
	yearsTopay = forms.FloatField()
	entry = forms.FloatField()
	energyconsume = forms.FloatField()
	radiation1 = forms.CharField()
	radiation2 = forms.FloatField()
	radiation3 = forms.FloatField()
	pricekwh=forms.FloatField()
	economy= forms.FloatField()
	painelpower= forms.FloatField()
	panelprice1= forms.CharField()
	panelprice2= forms.FloatField()
	panelprice3= forms.FloatField()
	priceinverters1= forms.CharField()
	priceinverters2= forms.FloatField()
	priceinverters3= forms.FloatField()
	pricestringbox= forms.FloatField()
	priceproject= forms.FloatField()
	pricewiring= forms.FloatField()
	pricess= forms.FloatField()
	pricelabor= forms.FloatField()
	maintenance1= forms.CharField()
	maintenance2= forms.FloatField()
	maintenance3= forms.FloatField()
	energy_production_tax=forms.FloatField()
	depreciation_years_inverters=forms.FloatField()
	depreciation_years_painels =forms.FloatField()
	person_or_business_or_sellenergy= forms.CharField()
	incometax=forms.FloatField()
	sim_year=forms.FloatField()
	inflation= forms.FloatField()
	ccp1= forms.CharField()
	ccp2= forms.FloatField()
	ccp3= forms.FloatField()
	cct1= forms.CharField()
	cct2= forms.FloatField()
	cct3= forms.FloatField()
	pccp= forms.FloatField()
	pcct= forms.FloatField()
	plifespan1= forms.FloatField()
	plifespan2= forms.FloatField()
	plifespan3= forms.FloatField()
	plifespan4= forms.FloatField()
	plifespan5= forms.FloatField()
	plifespan6= forms.FloatField()
	plifespan7= forms.FloatField()
	ilifespan1= forms.FloatField()
	ilifespan2= forms.FloatField()
	ilifespan3= forms.FloatField()
	ilifespan4= forms.FloatField()
	ilifespan5= forms.FloatField()
	ilifespan6= forms.FloatField()
	ilifespan7= forms.FloatField()
	preduction= forms.FloatField()
	projeto= forms.CharField()
class testforms(forms.Form):
	antigo = forms.CharField()
	novo = forms.CharField()
class loginform(forms.Form):
	nome = forms.CharField()
	senha = forms.CharField()
	