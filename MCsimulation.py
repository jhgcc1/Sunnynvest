import Snumath
from Random import rnd
from Random import rndCustom
import numpy as np

def simMC(objIpunt):
    boleanIRR=False
    bolNegativeProhibitedInput=False
    simMC_result={}
    #objIpunt["depreciation_percentage_painels"]=(100/objIpunt["depreciation_years_painels"])/100
    #objIpunt["depreciation_percentage_inverters"]=(100/objIpunt["depreciation_years_inverters"])/100
    print("2")
    print(objIpunt["sim_year"])
    for SimulationYear in range(0,objIpunt["sim_year"]):
        rd_distMaintenance=rnd(objIpunt["distMaintenance"])
        rd_distPricePanel=rnd(objIpunt["distPricePanel"])# cant be negative
        if len(np.array(rd_distPricePanel)[np.where(np.array(rd_distPricePanel)<0)])!=0:
            return False
        rd_distPriceInv=rnd(objIpunt["distPriceInv"])# cant be negative
        if len(np.array(rd_distPriceInv)[np.where(np.array(rd_distPriceInv)<0)])!=0:
            return False
        rd_distRad=rnd(objIpunt["distRad"]) # cant be negative
        if len(np.array(rd_distRad)[np.where(np.array(rd_distRad)<0)])!=0:
            return False
        rd_distWcpp=rnd(objIpunt["distccp"])
        rd_distWcct=rnd(objIpunt["distcct"])
        rd_distIlifespan=rndCustom(objIpunt["distIlifespan"])
        rd_distPlifespan=rndCustom(objIpunt["distPlifespan"])
        temporary_list_inputs=[rd_distPriceInv,rd_distPricePanel,rd_distMaintenance,rd_distWcct,rd_distRad,rd_distWcpp,rd_distIlifespan,rd_distPlifespan]

        SimulationYearString=str(SimulationYear)
        for simNum in range(0,len(rd_distRad)):
            mantenanceS=rd_distMaintenance[simNum]
            pricepainelS=rd_distPricePanel[simNum]
            priceinvertersS=rd_distPriceInv[simNum]
            radiationS=rd_distRad[simNum]
            cctS=rd_distWcct[simNum]
            ccpS=rd_distWcpp[simNum]
            ilifespanS=rd_distIlifespan[simNum]
            plifespanS=rd_distPlifespan[simNum]
            label_year,label_year_simulation,year = Snumath.lebals_years(plifespanS,SimulationYear)
            ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(objIpunt["energyconsume"],objIpunt["economy"],radiationS,objIpunt["painelpower"],pricepainelS,objIpunt["sellOrComp"],objIpunt["npanel"])
            result_wacc=Snumath.wacc(objIpunt["person_or_business_or_sellenergy"],ccpS,cctS,objIpunt["pccp"],objIpunt["pcct"],objIpunt["inflation"],objIpunt["profittax"])
            result_wacc_no_inflation=Snumath.wacc_no_inflation(objIpunt["person_or_business_or_sellenergy"],ccpS,cctS,objIpunt["pccp"],objIpunt["pcct"],objIpunt["profittax"])
            result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
            array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,plifespanS,objIpunt["pricekwh"],wplantpower,mwplantpower,kwplantpower,objIpunt["initial_pefficiency"],radiationS,objIpunt["preduction"],objIpunt["energy_production_tax"])
            total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,priceinvertersS,objIpunt["pricestringbox"],objIpunt["priceproject"],objIpunt["pricewiring"],objIpunt["pricess"],objIpunt["pricelabor"],objIpunt["priceothers"],SimulationYear,objIpunt["depreciation_years_painels"],objIpunt["depreciation_percentage_inverters"],objIpunt["depreciation_percentage_painels"],year,ilifespanS,plifespanS,objIpunt["depreciation_years_inverters"])
            priceperKWp=total_initial_investment[0]/wplantpower
            array_maintenance=Snumath.maintenanceF(mantenanceS,ndeplacas,plifespanS)
            total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,objIpunt["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,objIpunt["profittax"],array_maintenance,plifespanS,objIpunt["sellOrComp"])
            array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(objIpunt["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
            npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,ccpS,array_total_cashflow_noinflation,result_wacc_no_inflation,plifespanS,array_cashflow_negative,array_KWhenergy_per_year)
            if irr=="nan":
                print(irr)
                print(array_total_cashflow_inflation)
                boleanIRR=True

            pb=Snumath.FinancialSimulation(result_wacc_no_inflation,plifespanS,npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation)
            if boleanIRR:
                fvReinvestIRR="nan"
            else:
                fvReinvestIRR=np.fv(irr, plifespanS, 0,-total_initial_investment[0])
            fvReinvestMIRR=np.fv(mirr, plifespanS, 0,-total_initial_investment[0])
            temporary_list_outputs=[priceperKWp,spayback,total_initial_investment[0],irr,npv,mirr,vul,cost_per_kwh,lcoe,pb,fvReinvestIRR,fvReinvestMIRR]
            if SimulationYearString not in simMC_result:
                simMC_result[SimulationYearString]={"inputs":{"priceinverters":{"mean":0,"std":0,"rawData":[]},"pricepanel":{"mean":0,"std":0,"rawData":[]},"Maintenance":{"mean":0,"std":0,"rawData":[]},"Cost of debit":{"mean":0,"std":0,"rawData":[]},"Irradiation":{"mean":0,"std":0,"rawData":[]},"Cost of equity":{"mean":0,"std":0,"rawData":[]},"Inverters lifespan":{"mean":0,"std":0,"rawData":[]},"Panels lifespan":{"mean":0,"std":0,"rawData":[]}},"outputs":{"Price per KWp":{"mean":0,"std":0,"rawData":[]},"Simple payback":{"mean":0,"std":0,"rawData":[]},"Total investment":{"mean":0,"std":0,"rawData":[]},"IRR":{"mean":0,"std":0,"rawData":[]},"NPV":{"mean":0,"std":0,"rawData":[]},"MIRR":{"mean":0,"std":0,"rawData":[]},"Equivalent annual annuity":{"mean":0,"std":0,"rawData":[]},"Cost/kwh":{"mean":0,"std":0,"rawData":[]},"LCOE":{"mean":0,"std":0,"rawData":[]},"Discounted payback":{"rawData":[]},"Future value (IRR rate)":{"mean":0,"std":0,"rawData":[]},"Future value (MIRR rate)":{"mean":0,"std":0,"rawData":[]}}}
            for index,item in enumerate(simMC_result[SimulationYearString]["outputs"]):
                simMC_result[SimulationYearString]["outputs"][item]["rawData"].append(temporary_list_outputs[index])
        for item in simMC_result[SimulationYearString]["outputs"]:
            if(item!="Discounted payback"):
                if (("IRR" in item) and boleanIRR==False) or "IRR" not in item:
                    simMC_result[SimulationYearString]["outputs"][item]["mean"]=np.mean(simMC_result[SimulationYearString]["outputs"][item]["rawData"])
                    simMC_result[SimulationYearString]["outputs"][item]["std"]=np.std(simMC_result[SimulationYearString]["outputs"][item]["rawData"])
                else:
                    simMC_result[SimulationYearString]["outputs"][item]["mean"]="IRR with multiple roots"
                    simMC_result[SimulationYearString]["outputs"][item]["std"]="IRR with multiple roots"
            else:
                print(item)
                auxList=simMC_result[SimulationYearString]["outputs"][item]["rawData"]
                auxList.sort()
                simMC_result[SimulationYearString]["outputs"][item]["rawData"]=auxList
        for index,item in enumerate(simMC_result[SimulationYearString]["inputs"]):
            simMC_result[SimulationYearString]["inputs"][item]["rawData"]=temporary_list_inputs[index]
            simMC_result[SimulationYearString]["inputs"][item]["mean"]=np.mean(temporary_list_inputs[index])
            simMC_result[SimulationYearString]["inputs"][item]["std"]=np.std(temporary_list_inputs[index])
            if(item=="Inverters lifespan" or item=="Panels lifespan"):
                auxList=simMC_result[SimulationYearString]["inputs"][item]["rawData"]
                auxList.sort()
                simMC_result[SimulationYearString]["inputs"][item]["rawData"]=auxList
    return simMC_result
        

