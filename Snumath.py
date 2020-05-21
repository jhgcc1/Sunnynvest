
import numpy as np	
from datetime import datetime
from math import log10
""" energyconsume = 300
#radiation = 4.8
pricekwh= 0.6
economy= 0.8
painelpower= 300
pricepainel= 700
priceinverters= 3000
pricestringbox= 200
priceproject= 100
pricewiring= 300
pricess=500
pricelabor= 600
maintenance= 60
inflation= 0.05
ccp= 0.12
cct= 0.15
pccp= 0.6
pcct= 0.4
plifespan= 25
ilifespan= 12
preduction= 0.008
projeto= "teste"

#adicionar estas variaveis
inflation 
priceothers=0
profittax=0.25
person_or_business_or_sellenergy='Business'
depreciation_years_painels=25# less or equal than plifespan
depreciation_percentage_painels=(100/depreciation_years_painels)/100
depreciation_years_inverters=12# less or equal than ilifespan
depreciation_percentage_inverters=(100/depreciation_years_inverters)/100
energy_production_tax=0
carbon_red=0.932
numberofyears_topay=10
simulation_period=3
entry=1000
#aux variable
initial_pefficiency=1
""" 

#label years
def lebals_years(plifespan,simulation_period):
    #today's date
    today = datetime.today()
    year= today.year
    label_year=[x for x in range(year,year+plifespan+1)]
    label_year_simulation=[x for x in range(year,year+simulation_period+1)]
    return label_year,label_year_simulation,year

def InitialCalculations(energyconsume,economy,radiation,painelpower,pricepainel):
    #number of needed painels
    ndeplacas=int(energyconsume*economy/(((radiation)*30*painelpower)/1000))
    #total investment in painels
    invest_painels=ndeplacas*pricepainel
    #maximum economy achieved
    maxeconomy=str(((((radiation*painelpower*ndeplacas*30)/1000)/energyconsume)*100))+'%'
    #plant power
    wplantpower=(ndeplacas*painelpower)
    kwplantpower=wplantpower/1000
    mwplantpower=kwplantpower/1000

    return ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower


#Wacc inflationated function and call
def wacc(person_or_business_or_sellenergy,ccp,cct,pccp,pcct,inflation,profittax):
    if person_or_business_or_sellenergy=='Person':
        result_wacc=ccp*pccp+cct*pcct+inflation+((ccp*pccp+cct*pcct)*inflation)
        return result_wacc
    else:
        result_wacc=ccp*pccp+cct*(1-profittax)*pcct+inflation+((ccp*pccp+cct*(1-profittax)*pcct)*inflation)
        return result_wacc

#wacc without inflation
def wacc_no_inflation(person_or_business_or_sellenergy,ccp,cct,pccp,pcct,profittax):
    if person_or_business_or_sellenergy=='Person':
        result_wacc_no_inflation=ccp*pccp+cct*pcct
        return result_wacc_no_inflation
    else:
        result_wacc_no_inflation=ccp*pccp+cct*(1-profittax)*pcct
        return result_wacc_no_inflation

#wacc monthly without inflation
def wacc_m_no_inflation(result_wacc_no_inflation):
    result_wacc_m_no_inflation=10**((log10(1+result_wacc_no_inflation)/12))-1
    return result_wacc_m_no_inflation

#energy production and gross revenue
def energyProduction(result_wacc_m_no_inflation,plifespan,pricekwh,wplantpower,mwplantpower,kwplantpower,initial_pefficiency,radiation,preduction,energy_production_tax):
    Whenergy_per_year=[0]
    MWhenergy_per_year=[0]
    KWhenergy_per_year=[0]
    array_gross_revenue=[0]
    for ano in range(1,plifespan+1):
        Whenergy_per_year.append(wplantpower*initial_pefficiency*radiation*365)
        MWhenergy_per_year.append(mwplantpower*initial_pefficiency*radiation*365)
        KWhenergy_per_year.append(kwplantpower*initial_pefficiency*radiation*365)
        initial_pefficiency=initial_pefficiency*(1-preduction)
        gross_revenue_anual=KWhenergy_per_year[ano]*pricekwh*(1-energy_production_tax)
        gross_f_revenue=0
        for month in range(0,12):
            gross_f_revenue=gross_f_revenue+np.fv(result_wacc_m_no_inflation,month,0,-(gross_revenue_anual/12))
        array_gross_revenue.append(gross_f_revenue)
    array_gross_revenue=np.array(array_gross_revenue)
    array_Whenergy_per_year=np.array(Whenergy_per_year)
    array_KWhenergy_per_year=np.array(KWhenergy_per_year)
    array_MWhenergy_per_year=np.array(MWhenergy_per_year)
    return array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year



#inverters and painels depreciation and reinvestments
def derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,priceinverters,pricestringbox,priceproject,pricewiring,pricess,pricelabor,priceothers,simulation_period,depreciation_years_painels,depreciation_percentage_inverters,depreciation_percentage_painels,year,ilifespan,plifespan,depreciation_years_inverters):
    diferenca_regressao=year+simulation_period-2016
    priceinverters=priceinverters*(1-((1.0531*2.71828182845904**(-0.132*(8+diferenca_regressao)))-(1.0531*2.71828182845904**(-0.132*(simulation_period+8+diferenca_regressao)))))
    array_inverterinv_pear_year_bolean=np.array([1 if x % ilifespan==0 and x!=0 else 0 for x in range(0,plifespan+1)])
    array_inverterinv_pear_year_bolean2=np.array([x if x % depreciation_years_inverters==0 and x!=0 else 0 for x in range(0,plifespan+1)])
    array_inverter_future_value=np.array([1-((1.0531*2.71828182845904**(-0.132*(8+diferenca_regressao)))-(1.0531*2.71828182845904**(-0.132*(x+8+diferenca_regressao)))) for x in range(0,plifespan+1)])
    array_investmentinvertes=array_inverterinv_pear_year_bolean*array_inverter_future_value*priceinverters
    array_depreciation_painels=np.array([invest_painels*depreciation_percentage_painels if x<=depreciation_years_painels and x!=0 else 0 for x in range(0,plifespan+1)])
    #dynamic inverter dep
    array_inv_bolean_future=array_inverterinv_pear_year_bolean*array_inverter_future_value
    inv_useful_units=array_inv_bolean_future[array_inv_bolean_future != 0]
    inv_useful_units2=array_inverterinv_pear_year_bolean2[array_inverterinv_pear_year_bolean2!=0]
    inv_useful_units=list(inv_useful_units)
    inv_useful_units.insert(0,1)
    dep_year_1=[]
    dep_year_total=np.array([0])
    y=0
    dep_gap= ilifespan-depreciation_years_inverters
    for vl in inv_useful_units:
        dep_year_1=[inv_useful_units[y]*priceinverters*depreciation_percentage_inverters for x in range(1,inv_useful_units2[0]+1)]
        dep_year_total=np.append(dep_year_total,dep_year_1)
        y+=1
        for ano in range(0,dep_gap):
            dep_year_total=np.append(dep_year_total,[0])
            year+=year
    array_depreciation_inverters=dep_year_total[:plifespan+1]
    #residual vlaue invrter
    last_year=""
    number_inv_inverters=0
    for bolean in range(plifespan,-1,-1):
        if array_inverterinv_pear_year_bolean[bolean]!=0:
            if last_year=="":
                last_year=bolean
            number_inv_inverters+=1
    residual_value_inverters=array_inverter_future_value[last_year]*priceinverters-((plifespan-last_year)*priceinverters*array_inverter_future_value[last_year]*depreciation_percentage_inverters)
    array_residual_value_inverters=np.array([residual_value_inverters if x==plifespan else 0 for x in range(0,plifespan+1)])
    #array_total_investement
    total_initial_investment=[((invest_painels+priceinverters+pricestringbox+priceproject+pricewiring+pricess+pricelabor+priceothers)*(1-((1.0531*2.71828182845904**(-0.132*(8+diferenca_regressao)))-(1.0531*2.71828182845904**(-0.132*(simulation_period+8+diferenca_regressao)))))) if x ==0 else 0 for x in range(0,plifespan+1)]
    return total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters

#maintenace
def maintenanceF(maintenance,ndeplacas,plifespan):
    array_maintenance=np.array([maintenance*ndeplacas if x!=0 else 0 for x in range(0,plifespan+1)])
    return array_maintenance

#Fiscal effects
def fiscal_effects(array_gross_revenue,person_or_business_or_sellenergy,array_depreciation_inverters,array_depreciation_painels,profittax,array_maintenance,plifespan):
    if person_or_business_or_sellenergy=='Business':
        array_ficaleffects_positive=(array_depreciation_inverters+array_depreciation_painels+array_maintenance)*profittax
        array_ficaleffects_negative=(array_gross_revenue*profittax)
        total_fiscaleffets=array_ficaleffects_positive-array_ficaleffects_negative
    elif person_or_business_or_sellenergy=='Person':
        total_fiscaleffets=np.array([0 for x in range(0,plifespan+1)])
    elif person_or_business_or_sellenergy=='Sell energy':
        array_ficaleffects_positive=(array_depreciation_inverters+array_depreciation_painels+array_maintenance)*profittax
        array_ficaleffects_negative=np.array([0 for x in range(0,plifespan+1)])
        total_fiscaleffets=array_ficaleffects_positive-array_ficaleffects_negative
    return total_fiscaleffets

#no inflation cashflow
def cash_flow_no_inflation_and_inflation(inflation,total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets):
    array_cashflow_positive=array_gross_revenue+array_residual_value_inverters+total_fiscaleffets
    array_cashflow_negative=array_maintenance+array_investmentinvertes+total_initial_investment
    array_total_cashflow_noinflation=array_cashflow_positive-array_cashflow_negative
    #inflationated cashflow
    array_total_cashflow_inflation=[]
    n=0
    for vl in array_total_cashflow_noinflation:
        array_total_cashflow_inflation.append(np.fv(inflation,n,0,-vl))
        n+=1
    array_total_cashflow_inflation=np.array(array_total_cashflow_inflation)
    return array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative

def FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,ccp,array_total_cashflow_noinflation,result_wacc_no_inflation,plifespan,array_cashflow_negative,array_KWhenergy_per_year):
    #Npv
    npv=np.npv(result_wacc,array_total_cashflow_inflation)
    #irr
    irr=np.irr(array_total_cashflow_inflation)
    #mirr
    mirr=np.mirr(array_total_cashflow_inflation,result_wacc,ccp)
    spayback=-array_total_cashflow_noinflation[0]/array_total_cashflow_noinflation[1]
    #VUL
    pmt=np.pmt(result_wacc_no_inflation,plifespan,npv)
    vul=-pmt
    #cost/KWh
    cost_per_kwh=np.npv(result_wacc_no_inflation,array_cashflow_negative)/np.sum(array_KWhenergy_per_year)
    #lCOE
    lcoe=np.npv(result_wacc_no_inflation,array_cashflow_negative)/np.npv(result_wacc_no_inflation,array_KWhenergy_per_year)
    return npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe

def FinancialSimulation(result_wacc_no_inflation,plifespan,npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation):
    array_discounted_payback=np.array([np.npv(result_wacc,array_total_cashflow_inflation[0:x]) for x in range(1,plifespan+2)])
    if array_discounted_payback[0]>0:
        return "first input of cash flow cant be negative"
    else:
        array_discounted_payback_reversed=array_discounted_payback[::-1]
        lenght=len(array_discounted_payback)
        pb=0
        for index,npv in enumerate(array_discounted_payback_reversed):
            if index!=lenght-1:
                if npv>=0  and array_discounted_payback_reversed[index+1]<0:
                    discounted_payback_after_last_sign_change = np.array(array_discounted_payback_reversed[0:index])
                    supportArray=discounted_payback_after_last_sign_change[np.where( discounted_payback_after_last_sign_change < 0 )]
                    if len(supportArray)==0:
                        pb=lenght-index-1
                    break
        return pb

def Static(invest_painels,priceinverters,pricestringbox,priceproject,pricewiring,pricess,pricelabor,priceothers,entry,carbon_red,array_KWhenergy_per_year,plifespan,array_gross_revenue,inflation,array_total_cashflow_noinflation,result_wacc,array_total_cashflow_inflation,numberofyears_topay,result_wacc_no_inflation):
    #carbonsaved 0.932 kg of carbon dioxide emission reduction per KWh
    array_co2_reduction=np.array([carbon_red*array_KWhenergy_per_year[x] for x in range(0,plifespan+1)])
    #summed energy produced
    sum_array_KWhenergy_per_year=np.array([np.sum(array_KWhenergy_per_year[0:x]) for x in range(1,plifespan+2)])
    #summed revenew
    sum_array_gross_revenue=np.array([np.sum(array_gross_revenue[0:x]) for x in range(1,plifespan+2)])
    #inflationated sum reveneu
    sum_array_gross_revenue_inf=np.array([np.fv(inflation,x-2,0,-np.sum(array_gross_revenue[0:x])) for x in range(1,plifespan+2)])
    #simplepayback
    spayback=-array_total_cashflow_noinflation[0]/array_total_cashflow_noinflation[1]
    #discounted payback
    array_discounted_payback=np.array([np.npv(result_wacc,array_total_cashflow_inflation[0:x]) for x in range(1,plifespan+2)])
    #annuity cashflow inflationated 
    array_annuity_inflation= np.array([-np.pmt(result_wacc,numberofyears_topay,array_total_cashflow_inflation[0]+entry) if x != 0 and x <= numberofyears_topay  else 0 for x in range(0,plifespan+1)])
    array_annuity_inflation_cashflow=array_annuity_inflation+array_total_cashflow_inflation
    array_annuity_inflation_cashflow[0]=-entry
    #annuity cashflow non inflationated
    array_annuity_noinflation= np.array([-np.pmt(result_wacc_no_inflation,numberofyears_topay,array_total_cashflow_noinflation[0]+entry) if x != 0 and x <= numberofyears_topay  else 0 for x in range(0,plifespan+1)])
    array_annuity_noinflation_cashflow=array_annuity_noinflation+array_total_cashflow_noinflation
    array_annuity_noinflation_cashflow[0]=-entry
    #annuity payment inflationated
    annuity_payment_inflation=array_annuity_inflation[0:numberofyears_topay+1]
    #annuity payment non inflationated
    annuity_payment_noinflation=array_annuity_noinflation[0:numberofyears_topay+1]
    #abc curver
    array_abc_values=np.array([invest_painels,priceinverters,pricestringbox,priceproject,pricewiring,pricess,pricelabor,priceothers])
    array_abc_curve_percentage=np.array([x/sum(array_abc_values) for x in array_abc_values])
    array_abc_curve_graph=np.array([sum(array_abc_curve_percentage[0:x]) for x in range(1,len(array_abc_curve_percentage)+1)])
    array_abc_curve_graph_xlabels=["Solar painels","Inverters","Stringboxs","Project","Wiring","Suport structures","Labor","Others"]
    array_abc_curve_percentage_list=array_abc_curve_percentage.tolist()
    objABC={
        "Solar painels":array_abc_curve_percentage_list[0],
        "Inverters":array_abc_curve_percentage_list[1],
        "Stringboxs":array_abc_curve_percentage_list[2],
        "Project":array_abc_curve_percentage_list[3],
        "Wiring":array_abc_curve_percentage_list[4],
        "Suport structures":array_abc_curve_percentage_list[5],
        "Labor":array_abc_curve_percentage_list[6],
        "Others":array_abc_curve_percentage_list[7],
    }
    abcList=objABC
    return abcList,array_co2_reduction,sum_array_KWhenergy_per_year,sum_array_gross_revenue,sum_array_gross_revenue_inf,spayback,array_discounted_payback,array_annuity_inflation_cashflow,array_annuity_noinflation_cashflow,annuity_payment_inflation,annuity_payment_noinflation


