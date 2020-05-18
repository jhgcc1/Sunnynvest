
from django.shortcuts import render , redirect
from pages.forms import registrationform, dadosform, testforms, loginform, changepass
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm 
from pages.models import dadosmodels, testmodels, uuprofile
from django.contrib.auth import authenticate, login as alogin, views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import update_session_auth_hash, logout
from django.core.mail import EmailMessage
from django.contrib import messages
import sys
import numpy as np
from SpiderGraph import spiderS
from MCsimulation import simMC
from StaticMaths import staticMaths
from django.shortcuts import get_object_or_404
import json

testenado=0
def home(request):
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	args=mandaremail(request,args)
	global testenado
	testenado = 10
	return render(request,"home.html",args)

def about(request):
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	args=mandaremail(request,args)
	return render(request,"about.html",args)

def contact(request):
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	args=mandaremail(request,args)
	return render(request,"contact.html",args)
def profile(request):
	
	modelos= dadosmodels.objects.filter(usuario=request.user)
	project=[]
	for item in modelos:
		project.append(item.projeto)
	print(project)
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	n=str(nomeoulogin)
	usernome=n[(n.index(','))+2:len(n)]
	args={"projects":project,'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile, 'email':email, 'pais':pais, 'nome':nome, 'nome2':nome2, 'usernome':usernome}
	args=mandaremail(request,args)
	if request.POST.get('pjbt'):
		projeto=request.POST.get('pj')
		comment=dadosmodels.objects.get(projeto=projeto)
		print("@w@")
		dictStringResult=comment.dictStringResult
		args["dictStringResult"]=dictStringResult
		return render(request,"Graphs.html",args)
	else:
		return render(request,"Profile.html",args)

def login(request):
	
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile, 'email':email}
	args=mandaremail(request,args)
	args["errorLogin"]="none"
	if request.method =='POST':
		form = loginform(request.POST)
		if form.is_valid():
			nome=request.POST.get('nome')
			senha=request.POST.get('senha')

			user = authenticate(request,username=nome, password=senha)
			if user is not None:
				alogin(request,user)
				
				return redirect('home')
			else:
				args["errorLogin"]="initial"
				return render(request,"login.html",args)
	else:
		return render(request,"login.html",args)
def login2(request):

	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile, 'email':email}
	args=mandaremail(request,args)
	args["errorLogin"]="none"
	if request.method =='POST':
		form = loginform(request.POST)
		if form.is_valid():
			nome=request.POST.get('nome')
			senha=request.POST.get('senha')

			user = authenticate(request,username=nome, password=senha)
			if user is not None:
				alogin(request,user)
				return redirect('input')
			else:
				args["errorLogin"]="initial"
				return render(request,"login.html",args)

	else:
		return render(request,"login.html",args)
def share(request,idpjn):
		nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
		args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
		args=mandaremail(request,args)
		try:
			clientShare=dadosmodels.objects.get(clientShare=idpjn)
		except:
			clientShare=None
		if clientShare!=None:
			dictStringResult=clientShare.dictStringResult
			args["dictStringResult"]=dictStringResult
			return render(request,"Graphs.html",args)
		else:
			return render(request,"ErrorProject.html",args)


def input(request):
	
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	args=mandaremail(request,args)
	if request.POST.get('calcular'):

		paymentMethod = request.POST.get('paymentMethod')
		if paymentMethod=="cash":
			yearsTopay=0
			entry=0
		else:
			yearsTopay = int(request.POST.get('yearsTopay'))
			entry = float(request.POST.get('entry'))
		energyconsume = float(request.POST.get('energyconsume'))
		radiation1 = request.POST.get('radiation1')
		radiation2 = float(request.POST.get('radiation2'))
		radiation3 = float(request.POST.get('radiation3'))
		pricekwh= float(request.POST.get('pricekwh'))
		economy= float(request.POST.get('economy'))
		painelpower= float(request.POST.get('painelpower'))
		panelprice1= request.POST.get('panelprice1')
		panelprice2= float(request.POST.get('panelprice2'))
		panelprice3= float(request.POST.get('panelprice3'))
		priceothers = float(request.POST.get('priceothers'))
		sim_year = request.POST.get('sim_year')
		priceinverters1= request.POST.get('priceinverters1')
		priceinverters2= float(request.POST.get('priceinverters2'))
		priceinverters3= float(request.POST.get('priceinverters3'))
		pricestringbox= float(request.POST.get('pricestringbox'))
		priceproject= float(request.POST.get('priceproject'))
		pricewiring= float(request.POST.get('pricewiring'))
		pricess= float(request.POST.get('pricess'))
		pricelabor= float(request.POST.get('pricelabor'))
		maintenance1= request.POST.get('maintenance1')
		maintenance2= float(request.POST.get('maintenance2'))
		maintenance3= float(request.POST.get('maintenance3'))
		inflation= float(request.POST.get('inflation'))
		ccp1= request.POST.get('ccp1')
		ccp2= float(request.POST.get('ccp2'))
		ccp3= float(request.POST.get('ccp3'))
		cct1= request.POST.get('cct1')
		cct2= float(request.POST.get('cct2'))
		cct3= float(request.POST.get('cct3'))
		pccp= float(request.POST.get('pccp'))
		pcct= float(request.POST.get('pcct'))
		plifespan1= request.POST.get('plifespan1')
		plifespan2= int(request.POST.get('plifespan2'))
		plifespan3= float(request.POST.get('plifespan3'))
		plifespan4= int(request.POST.get('plifespan4'))
		plifespan5= float(request.POST.get('plifespan5'))
		plifespan6= int(request.POST.get('plifespan6'))
		plifespan7= float(request.POST.get('plifespan7'))
		ilifespan1= request.POST.get('ilifespan1')
		ilifespan2= int(request.POST.get('ilifespan2'))
		ilifespan3= float(request.POST.get('ilifespan3'))
		ilifespan4= int(request.POST.get('ilifespan4'))
		ilifespan5= float(request.POST.get('ilifespan5'))
		ilifespan6= int(request.POST.get('ilifespan6'))
		ilifespan7= float(request.POST.get('ilifespan7'))
		preduction= float(request.POST.get('preduction'))
		incometax = float(request.POST.get('incometax'))
		person_or_business_or_sellenergy = request.POST.get('person_or_business_or_sellenergy')
		depreciation_years_painels = int(request.POST.get('depreciation_years_painels'))
		depreciation_years_inverters = int(request.POST.get('depreciation_years_inverters'))
		energy_production_tax = float(request.POST.get('energy_production_tax'))
		projeto= request.POST.get('projeto')
		usuario = request.user
		print(usuario)
		projeto= request.POST.get('projeto')
		print(projeto)
		Comment="ERRO"
		try:
			Comment=dadosmodels.objects.get(projeto=projeto,usuario=usuario)
		except:
			Comment=None
		print("Comment")
		print(Comment)
		if Comment==None:
			sim_year=int(request.POST.get('sim_year')[0:1])
			form = dadosform(request.POST)
			objIpunt={"energyconsume":energyconsume,
			"pricekwh":pricekwh,
			"paymentMethod":paymentMethod,
			"economy":economy/100,
			"painelpower":painelpower,
			"pricestringbox":pricestringbox,
			"priceproject":priceproject,
			"pricewiring":pricewiring,
			"pricess":pricess,
			"pricelabor":pricelabor,
			"inflation":inflation/100,
			"pccp":pccp/100,
			"pcct":pcct/100,
			"preduction":preduction/100,
			"priceothers":priceothers,
			"sim_year":int(request.POST.get('sim_year')[0:1]),
			"profittax":incometax/100,
			"person_or_business_or_sellenergy":person_or_business_or_sellenergy,
			"depreciation_years_painels":depreciation_years_painels,
			"depreciation_years_inverters":depreciation_years_inverters,
			"energy_production_tax":energy_production_tax,
			"initial_pefficiency":1,
			"distMaintenance":[maintenance1,maintenance2,maintenance3],
			"distPricePanel":[panelprice1,panelprice2,panelprice3],
			"distPriceInv":[priceinverters1,priceinverters2,priceinverters3],
			"distRad":[radiation1,radiation2,radiation3],
			"distccp":[ccp1,ccp2/100,ccp3/100],
			"distcct":[cct1,cct2/100,cct3/100],
			"yearsTopay":yearsTopay,
			"entry":entry,
			"carbon_red":0.932,
			"distIlifespan":[ilifespan1,{"value1":{"probability":ilifespan3/100,"value":ilifespan2},"value2":{"probability":ilifespan5/100,"value":ilifespan4},"value3":{"probability":ilifespan7/100,"value":ilifespan6}}],
			"distPlifespan":[plifespan1,{"value1":{"probability":plifespan3/100,"value":plifespan2},"value2":{"probability":plifespan5/100,"value":plifespan4},"value3":{"probability":plifespan7/100,"value":plifespan6}}]}
			objIpunt["depreciation_percentage_painels"]=(100/objIpunt["depreciation_years_painels"])/100
			objIpunt["depreciation_percentage_inverters"]=(100/objIpunt["depreciation_years_inverters"])/100
			simMC_result=simMC(objIpunt)
			print(simMC_result["0"]["inputs"])
			args["modeloPJname"]=False
			if objIpunt["distMaintenance"][0]=="Fixed value":
				print(simMC_result)
				objIpunt["maintenance"]=simMC_result["0"]["inputs"]["Maintenance"]["rawData"][0]
			else:
				objIpunt["maintenance"]=simMC_result["0"]["inputs"]["Maintenance"]["mean"]

			if objIpunt["distPricePanel"][0]=="Fixed value":
				objIpunt["pricepainel"]=simMC_result["0"]["inputs"]["pricepanel"]["rawData"][0]
			else:
				objIpunt["pricepainel"]=simMC_result["0"]["inputs"]["pricepanel"]["mean"]

			if objIpunt["distPriceInv"][0]=="Fixed value":
				objIpunt["priceinverters"]=simMC_result["0"]["inputs"]["priceinverters"]["rawData"][0]
			else:
				objIpunt["priceinverters"]=simMC_result["0"]["inputs"]["priceinverters"]["mean"]

			if objIpunt["distRad"][0]=="Fixed value":
				objIpunt["Irradiation"]=simMC_result["0"]["inputs"]["Irradiation"]["rawData"][0]
			else:
				objIpunt["Irradiation"]=simMC_result["0"]["inputs"]["Irradiation"]["mean"]

			if objIpunt["distccp"][0]=="Fixed value":
				objIpunt["ccp"]=simMC_result["0"]["inputs"]["Cost of equity"]["rawData"][0]
			else:
				objIpunt["ccp"]=simMC_result["0"]["inputs"]["Cost of equity"]["mean"]

			if objIpunt["distcct"][0]=="Fixed value":
				objIpunt["cct"]=simMC_result["0"]["inputs"]["Cost of debit"]["rawData"][0]
			else:
				objIpunt["cct"]=simMC_result["0"]["inputs"]["Cost of debit"]["mean"]

			if objIpunt["distIlifespan"][0]!="Custom probabilities":
				objIpunt["ilifespan"]=simMC_result["0"]["inputs"]["Inverters lifespan"]["rawData"][0]
			else:
				objIpunt["ilifespan"]=int(simMC_result["0"]["inputs"]["Inverters lifespan"]["mean"])
			if objIpunt["distPlifespan"][0]!="Custom probabilities":
				objIpunt["plifespan"]=simMC_result["0"]["inputs"]["Panels lifespan"]["rawData"][0]
			else:
				objIpunt["plifespan"]=int(simMC_result["0"]["inputs"]["Panels lifespan"]["mean"])
			print("aqui")
			print(objIpunt["plifespan"])
			print("aqui")
			print(objIpunt["ilifespan"])
			spiderS_result=spiderS(objIpunt)
			staticMaths_result=staticMaths(objIpunt)
			args["spiderS_result"]=spiderS_result
			args["simMC_result"]=simMC_result
			args["staticMaths_result"]=staticMaths_result

			clientShare=str(request.user)+"&"+projeto
			args["clientShare"]=clientShare

			dictStringResult={"clientShare":clientShare,"spiderS_result":spiderS_result,"simMC_result":simMC_result,"staticMaths_result":staticMaths_result}
			json.dumps(dictStringResult)
			
			dadosmodels_obj= dadosmodels(clientShare=clientShare,entry=entry,yearsTopay=yearsTopay,paymentMethod=paymentMethod,energyconsume=energyconsume, usuario=request.user,radiation1=radiation1,radiation2=radiation2,radiation3=radiation3,pricekwh=pricekwh,
			economy=economy,painelpower =painelpower,panelprice1=panelprice1,panelprice2=panelprice2,panelprice3=panelprice3,priceproject=priceproject,pricewiring=pricewiring,
			pricess=pricess,pricelabor=pricelabor,energy_production_tax=energy_production_tax,depreciation_years_inverters=depreciation_years_inverters,
			depreciation_years_painels=depreciation_years_painels,person_or_business_or_sellenergy=person_or_business_or_sellenergy,incometax=incometax,sim_year=sim_year,
			maintenance3=maintenance3,maintenance1=maintenance1,maintenance2=maintenance2,inflation=inflation,ccp1=ccp1,ccp2=ccp2,ccp3=ccp3,cct1=cct1,cct2=cct2,cct3=cct3,pccp=pccp,pcct=pcct,
			plifespan1=plifespan1,plifespan2=plifespan2,plifespan3=plifespan3,plifespan4=plifespan4,plifespan5=plifespan5,plifespan6=plifespan6,plifespan7=plifespan7,
			ilifespan1=ilifespan1,ilifespan2=ilifespan2,ilifespan3=ilifespan3,ilifespan4=ilifespan4,ilifespan5=ilifespan5,ilifespan6=ilifespan6,ilifespan7=ilifespan7,
			preduction=preduction,projeto=projeto,priceinverters1=priceinverters1,priceinverters2=priceinverters2,priceinverters3=priceinverters3,
			pricestringbox=pricestringbox,dictStringResult=dictStringResult)
			dadosmodels_obj.save()
			return render(request,'Graphs.html',args)
		else:
			paymentMethod = request.POST.get('paymentMethod')
			if paymentMethod=="cash":
				yearsTopay=0
				entry=0
			else:
				yearsTopay = int(request.POST.get('yearsTopay'))
				entry = float(request.POST.get('entry'))
			print(economy)
			objIpunt={"energyconsume":energyconsume,
			"pricekwh":pricekwh,
			"paymentMethod":paymentMethod,
			"economy":economy,
			"painelpower":painelpower,
			"pricestringbox":pricestringbox,
			"priceproject":priceproject,
			"pricewiring":pricewiring,
			"pricess":pricess,
			"pricelabor":pricelabor,
			"inflation":inflation,
			"pccp":pccp,
			"pcct":pcct,
			"preduction":preduction,
			"priceothers":priceothers,
			"sim_year":sim_year,
			"incometax":incometax,
			"person_or_business_or_sellenergy":person_or_business_or_sellenergy,
			"depreciation_years_painels":depreciation_years_painels,
			"depreciation_years_inverters":depreciation_years_inverters,
			"energy_production_tax":energy_production_tax,
			"initial_pefficiency":1,
			"maintenance":[maintenance1,maintenance2,maintenance3],
			"panelprice":[panelprice1,panelprice2,panelprice3],
			"priceinverters":[priceinverters1,priceinverters2,priceinverters3],
			"radiation":[radiation1,radiation2,radiation3],
			"ccp":[ccp1,ccp2,ccp3],
			"cct":[cct1,cct2,cct3],
			"yearsTopay":yearsTopay,
			"entry":entry,
			"carbon_red":0.932,
			"ilifespan":[ilifespan1,{"value1":{"probability":ilifespan3,"value":ilifespan2},"value2":{"probability":ilifespan5,"value":ilifespan4},"value3":{"probability":ilifespan7,"value":ilifespan6}}],
			"plifespan":[plifespan1,{"value1":{"probability":plifespan3,"value":plifespan2},"value2":{"probability":plifespan5,"value":plifespan4},"value3":{"probability":plifespan7,"value":plifespan6}}]}
			args["subargs"]=objIpunt
			args["modeloPJname"]=True
			return render(request,'input.html',args)

	else:
		form=dadosform()
		if request.user.is_authenticated:
			return render(request,"input.html",args)
		else:
			x='sim'
			return redirect('login2')

def register(request):
	nomeoulogin, logout, profile, email,pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	args=mandaremail(request,args)
	req=request.POST.get('username')
	if request.method =='POST':
		form = registrationform(request.POST)
		args['form']=form
		if form.is_valid():
			username=form.save()
			#uuprofile.objects.filter(user=username).update(country=str(request.POST.get('pais')))
			#uuprofile.objects.get(user=username).save()
			mudanca=uuprofile.objects.get(usuario=username)
			mudanca.country=str(request.POST.get('pais'))
			mudanca.save()
			modelo2 = True
			args['modelo2']=modelo2
			return redirect('login')
		else:
			return render(request,"register.html",args)

	else:
		form = registrationform()
		args['form']=form
		return render(request,"register.html",args)


def testpage(request):
	form=''
	nomeoulogin, logout, profile, email,pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	args=mandaremail(request,args)
	if request.method =='POST':
		form = changepass(request.user, request.POST)
		args['form']=form
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return render(request,"home.html",args)
		else:
			return render(request,"changepassword.html",args)
	else:
		form = changepass(request.user)
		args['form']=form
		return render(request,"changepassword.html",args)

def checarlogin(request):
	if request.user.is_authenticated:
		nomeoulogin='Welcome, ' + str(request.user)
		logout='Logout'
		profile='Profile'
		email=str(request.user.email)
		nome=str(request.user.first_name)
		nome2=str(request.user.last_name)
		pegarperfil= uuprofile.objects.get(usuario=request.user)
		pais=str(pegarperfil.country)
	else:
		nomeoulogin=''
		logout='Login'
		profile=''
		email=''
		nome=''
		nome2=''
		pais=''
		
	return nomeoulogin, logout, profile, email, pais, nome, nome2



def logoutt(request):
    logout(request)
    return redirect('home')


def mandaremail(request,args):

	if(request.GET.get('mybtn')):
		emailcliente=str(request.GET.get('emailend'))
		emailtext=str(request.GET.get('emailtext'))
		email = EmailMessage('Cliente: ' + emailcliente, emailtext, to=['jh_gcc@hotmail.com'])
		email.send()
		modelo = True
		args['modelo']=modelo
	return args
def fgt(request):

	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	args=mandaremail(request,args)
	args['forma'] = PasswordResetForm
	if request.method == 'POST':
		return PasswordResetView(request)

	else:
		return render(request,'forgotpassword.html',args)


def teste(request,var=None):
	if request.method =='GET':
		args={'var':var}
		return render(request,'test.html',args)





		





	







