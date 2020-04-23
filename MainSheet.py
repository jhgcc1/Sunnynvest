from SpiderGraph import spiderS
from MCsimulation import simMC
objIpunt={"energyconsume":300,
"pricekwh":0.6,
"economy":0.8,
"painelpower":300,
"pricestringbox":200,
"priceproject":100,
"pricewiring":300,
"pricess":500,
"pricelabor":600,
"inflation":0.05,
"pccp":0.6,
"pcct":0.4,
"preduction":0.008,
"priceothers":0,
"simulation_period":3,
"profittax":0.25,
"person_or_business_or_sellenergy":'Business',
"depreciation_years_painels":25,
"depreciation_years_inverters":12,
"energy_production_tax":0,
"initial_pefficiency":1,
"distMaintenance":["normal",60,30],
"distPricePanel":["normal",8200,1200],
"distPriceInv":["normal",8200,1200],
"distRad":["normal",4.8,1],
"distccp":["normal",18,2.5],
"distcct":["normal",18,2.5],
"distIlifespan":["mc",{"value1":{"probability":0.2,"value":5},"value2":{"probability":0.5,"value":10},"value3":{"probability":0.3,"value":15}}],
"distPlifespan":["mc",{"value1":{"probability":0.2,"value":20},"value2":{"probability":0.5,"value":25},"value3":{"probability":0.3,"value":30}}]}
objIpunt["depreciation_percentage_painels"]=(100/objIpunt["depreciation_years_painels"])/100
objIpunt["depreciation_percentage_inverters"]=(100/objIpunt["depreciation_years_inverters"])/100

simMC_result=simMC(objIpunt)
print(simMC_result)

if objIpunt["distMaintenance"][0]=="none":
    objIpunt["maintenance"]=simMC_result["0"]["inputs"]["maintenance"]["rawData"][0]
else:
    objIpunt["maintenance"]=simMC_result["0"]["inputs"]["maintenance"]["mean"]

if objIpunt["distPricePanel"][0]=="none":
    objIpunt["pricepainel"]=simMC_result["0"]["inputs"]["pricepainel"]["rawData"][0]
else:
    objIpunt["pricepainel"]=simMC_result["0"]["inputs"]["pricepainel"]["mean"]

if objIpunt["distPriceInv"][0]=="none":
    objIpunt["priceinverters"]=simMC_result["0"]["inputs"]["priceinverters"]["rawData"][0]
else:
    objIpunt["priceinverters"]=simMC_result["0"]["inputs"]["priceinverters"]["mean"]

if objIpunt["distRad"][0]=="none":
    objIpunt["radiation"]=simMC_result["0"]["inputs"]["radiation"]["rawData"][0]
else:
    objIpunt["radiation"]=simMC_result["0"]["inputs"]["radiation"]["mean"]

if objIpunt["distccp"][0]=="none":
    objIpunt["ccp"]=simMC_result["0"]["inputs"]["ccp"]["rawData"][0]
else:
    objIpunt["ccp"]=simMC_result["0"]["inputs"]["ccp"]["mean"]

if objIpunt["distcct"][0]=="none":
    objIpunt["cct"]=simMC_result["0"]["inputs"]["cct"]["rawData"][0]
else:
    objIpunt["cct"]=simMC_result["0"]["inputs"]["cct"]["mean"]

if objIpunt["distIlifespan"][0]=="none":
    objIpunt["ilifespan"]=simMC_result["0"]["inputs"]["Inverters lifespan"]["rawData"][0]
else:
    objIpunt["ilifespan"]=int(simMC_result["0"]["inputs"]["Inverters lifespan"]["mean"])

if objIpunt["distPlifespan"][0]=="none":
    objIpunt["plifespan"]=simMC_result["0"]["inputs"]["plifespan"]["rawData"][0]
else:
    objIpunt["plifespan"]=int(simMC_result["0"]["inputs"]["plifespan"]["mean"])

spiderS_result=spiderS(objIpunt)
print(spiderS_result)

