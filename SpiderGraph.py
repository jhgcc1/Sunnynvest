import Snumath
import numpy as np
def spiderS(obj):
    Irrbolean=False
    Result_spider={"Energy production":{"Sensitivity analysis Future value (MIRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR rate)":[],
    "Sensitivity analysis Future value (MIRR rate)":[],
    "Sensitivity analysis LCOE":[],
    "Sensitivity analysis Cost per KWh":[],
    "Sensitivity analysis Equivalent annual annuity":[],
    "Sensitivity analysis Simple Payback":[],
    "Sensitivity analysis IRR":[],"Sensitivity analysis NPV":[],
    "Sensitivity analysis MIRR":[],
    "Non-inflated IRR":[],
    "Non-inflated MIRR":[],
    "Future value IRR-Cost of equity (inflated)":[],
    "Future value IRR-Cost of equity (Non-inflated)":[],
    "Future value MIRR-Cost of equity (inflated)":[],
    "Future value MIRR-Cost of equity (Non-inflated)":[]},
    "Wacc":{"Sensitivity analysis Future value (MIRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR rate)":[],
    "Sensitivity analysis Future value (MIRR rate)":[],
    "Sensitivity analysis LCOE":[],
    "Sensitivity analysis Cost per KWh":[],
    "Sensitivity analysis Equivalent annual annuity":[],
    "Sensitivity analysis Simple Payback":[],
    "Sensitivity analysis IRR":[],
    "Sensitivity analysis NPV":[],
    "Sensitivity analysis MIRR":[],
    "Non-inflated IRR":[],
    "Non-inflated MIRR":[],
    "Future value IRR-Cost of equity (inflated)":[],
    "Future value IRR-Cost of equity (Non-inflated)":[],
    "Future value MIRR-Cost of equity (inflated)":[],
    "Future value MIRR-Cost of equity (Non-inflated)":[]},
    "Maintenance":{"Sensitivity analysis Future value (MIRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR rate)":[],
    "Sensitivity analysis Future value (MIRR rate)":[],
    "Sensitivity analysis LCOE":[],
    "Sensitivity analysis Cost per KWh":[],
    "Sensitivity analysis Equivalent annual annuity":[],
    "Sensitivity analysis Simple Payback":[],
    "Sensitivity analysis IRR":[],
    "Sensitivity analysis NPV":[],
    "Sensitivity analysis MIRR":[],
    "Non-inflated IRR":[],
    "Non-inflated MIRR":[],
    "Future value IRR-Cost of equity (inflated)":[],
    "Future value IRR-Cost of equity (Non-inflated)":[],
    "Future value MIRR-Cost of equity (inflated)":[],
    "Future value MIRR-Cost of equity (Non-inflated)":[]},
    "System price":{"Sensitivity analysis Future value (MIRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR rate)":[],
    "Sensitivity analysis Future value (MIRR rate)":[],
    "Sensitivity analysis LCOE":[],
    "Sensitivity analysis Cost per KWh":[],
    "Sensitivity analysis Equivalent annual annuity":[],
    "Sensitivity analysis Simple Payback":[],
    "Sensitivity analysis IRR":[],
    "Sensitivity analysis NPV":[],
    "Sensitivity analysis MIRR":[],
    "Non-inflated IRR":[],
    "Non-inflated MIRR":[],
    "Future value IRR-Cost of equity (inflated)":[],
    "Future value IRR-Cost of equity (Non-inflated)":[],
    "Future value MIRR-Cost of equity (inflated)":[],
    "Future value MIRR-Cost of equity (Non-inflated)":[]},
    "Panel lifespan":{"Sensitivity analysis Future value (MIRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR rate)":[],
    "Sensitivity analysis Future value (MIRR rate)":[],
    "Sensitivity analysis LCOE":[],
    "Sensitivity analysis Cost per KWh":[],
    "Sensitivity analysis Equivalent annual annuity":[],
    "Sensitivity analysis Simple Payback":[],
    "Sensitivity analysis IRR":[],
    "Sensitivity analysis NPV":[],
    "Sensitivity analysis MIRR":[],
    "Non-inflated IRR":[],
    "Non-inflated MIRR":[],
    "Future value IRR-Cost of equity (inflated)":[],
    "Future value IRR-Cost of equity (Non-inflated)":[],
    "Future value MIRR-Cost of equity (inflated)":[],
    "Future value MIRR-Cost of equity (Non-inflated)":[]},
    "Inverter lifespan":{"Sensitivity analysis Future value (MIRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR Non-inflated rate)":[],
    "Sensitivity analysis Future value (IRR rate)":[],
    "Sensitivity analysis Future value (MIRR rate)":[],
    "Sensitivity analysis LCOE":[],
    "Sensitivity analysis Cost per KWh":[],
    "Sensitivity analysis Equivalent annual annuity":[],
    "Sensitivity analysis Simple Payback":[],
    "Sensitivity analysis IRR":[],
    "Sensitivity analysis NPV":[],
    "Sensitivity analysis MIRR":[],
    "Non-inflated IRR":[],
    "Non-inflated MIRR":[],
    "Future value IRR-Cost of equity (inflated)":[],
    "Future value IRR-Cost of equity (Non-inflated)":[],
    "Future value MIRR-Cost of equity (inflated)":[],
    "Future value MIRR-Cost of equity (Non-inflated)":[]}}

    rangeSpider=[x for x in range(-50,50,3)]
    label_year,label_year_simulation,year = Snumath.lebals_years(obj["plifespan"],obj["sim_year"])
    for percent in rangeSpider:
        percentage = percent/100
        #energy
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"],obj["sellOrComp"],obj["npanel"])
        kwplantpower=kwplantpower+(kwplantpower*percentage)
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"],obj["sellOrComp"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        mirrNinf,irrNinf,npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year,obj["cct"])
        #ccpSInf=obj["ccp"]+obj["inflation"]+(obj["ccp"]*obj["inflation"])
        fvCCPS=np.fv(obj["ccp"],obj["plifespan"], 0,-total_initial_investment[0])
        fvCCPSinf=fvCCPS
        
        if irr=="nan" or irrNinf=="nan":
            print(irr)
            print(array_total_cashflow_inflation)
            Irrbolean=True

        pb=Snumath.FinancialSimulation(result_wacc_no_inflation,obj["plifespan"],npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation)
        if Irrbolean:
            fvReinvestIRR="nan"
            fvReinvestIRRNoinf="nan"
            dfvIrrCcpInf="nan"
            dfvIrrCcpNoInf="nan"
            irrNinf="nan"
        else:
            fvReinvestIRR=np.fv(irr, obj["plifespan"], 0,-total_initial_investment[0])
            fvReinvestIRRNoinf=np.fv(irrNinf, obj["plifespan"], 0,-total_initial_investment[0])
            dfvIrrCcpInf=fvReinvestIRR-fvCCPSinf
            dfvIrrCcpNoInf=fvReinvestIRRNoinf-fvCCPS

        
        fvReinvestMIRR=np.fv(mirr, obj["plifespan"], 0,-total_initial_investment[0])
        fvReinvestMIRRNoinf=np.fv(mirrNinf, obj["plifespan"], 0,-total_initial_investment[0])

        dfvMirrCcpInf=fvReinvestMIRR-fvCCPSinf
        dfvMirrCcpNoInf=fvReinvestMIRRNoinf-fvCCPS
        Result_spider["Energy production"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Energy production"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Energy production"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Energy production"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Energy production"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Energy production"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Energy production"]["Sensitivity analysis Cost per KWh"].append(cost_per_kwh)
        Result_spider["Energy production"]["Sensitivity analysis Future value (IRR rate)"].append(fvReinvestIRR)
        Result_spider["Energy production"]["Sensitivity analysis Future value (MIRR rate)"].append(fvReinvestMIRR)
        Result_spider["Energy production"]["Sensitivity analysis Future value (IRR Non-inflated rate)"].append(fvReinvestIRRNoinf)
        Result_spider["Energy production"]["Sensitivity analysis Future value (MIRR Non-inflated rate)"].append(fvReinvestMIRRNoinf)
        Result_spider["Energy production"]["Non-inflated IRR"].append(irrNinf)
        Result_spider["Energy production"]["Non-inflated MIRR"].append(mirrNinf)
        Result_spider["Energy production"]["Future value IRR-Cost of equity (inflated)"].append(dfvIrrCcpInf)
        Result_spider["Energy production"]["Future value IRR-Cost of equity (Non-inflated)"].append(dfvIrrCcpNoInf)
        Result_spider["Energy production"]["Future value MIRR-Cost of equity (inflated)"].append(dfvMirrCcpInf)
        Result_spider["Energy production"]["Future value MIRR-Cost of equity (Non-inflated)"].append(dfvMirrCcpNoInf)

        #maintenance
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"],obj["sellOrComp"],obj["npanel"])
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        array_maintenance=array_maintenance+(array_maintenance*percentage)
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"],obj["sellOrComp"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        mirrNinf,irrNinf,npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year,obj["cct"])
        #ccpSInf=obj["ccp"]+obj["inflation"]+(obj["ccp"]*obj["inflation"])
        fvCCPS=np.fv(obj["ccp"],obj["plifespan"], 0,-total_initial_investment[0])
        fvCCPSinf=fvCCPS
        
        if irr=="nan" or irrNinf=="nan":
            print(irr)
            print(array_total_cashflow_inflation)
            Irrbolean=True

        pb=Snumath.FinancialSimulation(result_wacc_no_inflation,obj["plifespan"],npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation)
        if Irrbolean:
            fvReinvestIRR="nan"
            fvReinvestIRRNoinf="nan"
            dfvIrrCcpInf="nan"
            dfvIrrCcpNoInf="nan"
            irrNinf="nan"
        else:
            fvReinvestIRR=np.fv(irr, obj["plifespan"], 0,-total_initial_investment[0])
            fvReinvestIRRNoinf=np.fv(irrNinf, obj["plifespan"], 0,-total_initial_investment[0])
            dfvIrrCcpInf=fvReinvestIRR-fvCCPSinf
            dfvIrrCcpNoInf=fvReinvestIRRNoinf-fvCCPS

        
        fvReinvestMIRR=np.fv(mirr, obj["plifespan"], 0,-total_initial_investment[0])
        fvReinvestMIRRNoinf=np.fv(mirrNinf, obj["plifespan"], 0,-total_initial_investment[0])

        dfvMirrCcpInf=fvReinvestMIRR-fvCCPSinf
        dfvMirrCcpNoInf=fvReinvestMIRRNoinf-fvCCPS
        Result_spider["Maintenance"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Maintenance"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Maintenance"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Maintenance"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Maintenance"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Maintenance"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Maintenance"]["Sensitivity analysis Cost per KWh"].append(cost_per_kwh)
        Result_spider["Maintenance"]["Sensitivity analysis Future value (IRR rate)"].append(fvReinvestIRR)
        Result_spider["Maintenance"]["Sensitivity analysis Future value (MIRR rate)"].append(fvReinvestMIRR)
        Result_spider["Maintenance"]["Sensitivity analysis Future value (IRR Non-inflated rate)"].append(fvReinvestIRRNoinf)
        Result_spider["Maintenance"]["Sensitivity analysis Future value (MIRR Non-inflated rate)"].append(fvReinvestMIRRNoinf)
        Result_spider["Maintenance"]["Non-inflated IRR"].append(irrNinf)
        Result_spider["Maintenance"]["Non-inflated MIRR"].append(mirrNinf)
        Result_spider["Maintenance"]["Future value IRR-Cost of equity (inflated)"].append(dfvIrrCcpInf)
        Result_spider["Maintenance"]["Future value IRR-Cost of equity (Non-inflated)"].append(dfvIrrCcpNoInf)
        Result_spider["Maintenance"]["Future value MIRR-Cost of equity (inflated)"].append(dfvMirrCcpInf)
        Result_spider["Maintenance"]["Future value MIRR-Cost of equity (Non-inflated)"].append(dfvMirrCcpNoInf)
        #inverters lifepsan
        ilifespanSpider=int(obj["ilifespan"])+int(obj["ilifespan"]*percentage)
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"],obj["sellOrComp"],obj["npanel"])
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,ilifespanSpider,obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"],obj["sellOrComp"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        mirrNinf,irrNinf,npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year,obj["cct"])
        #ccpSInf=obj["ccp"]+obj["inflation"]+(obj["ccp"]*obj["inflation"])
        fvCCPS=np.fv(obj["ccp"],obj["plifespan"], 0,-total_initial_investment[0])
        fvCCPSinf=fvCCPS
        
        if irr=="nan" or irrNinf=="nan":
            print(irr)
            print(array_total_cashflow_inflation)
            Irrbolean=True

        pb=Snumath.FinancialSimulation(result_wacc_no_inflation,obj["plifespan"],npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation)
        if Irrbolean:
            fvReinvestIRR="nan"
            fvReinvestIRRNoinf="nan"
            dfvIrrCcpInf="nan"
            dfvIrrCcpNoInf="nan"
            irrNinf="nan"
        else:
            fvReinvestIRR=np.fv(irr, obj["plifespan"], 0,-total_initial_investment[0])
            fvReinvestIRRNoinf=np.fv(irrNinf, obj["plifespan"], 0,-total_initial_investment[0])
            dfvIrrCcpInf=fvReinvestIRR-fvCCPSinf
            dfvIrrCcpNoInf=fvReinvestIRRNoinf-fvCCPS

        
        fvReinvestMIRR=np.fv(mirr, obj["plifespan"], 0,-total_initial_investment[0])
        fvReinvestMIRRNoinf=np.fv(mirrNinf, obj["plifespan"], 0,-total_initial_investment[0])

        dfvMirrCcpInf=fvReinvestMIRR-fvCCPSinf
        dfvMirrCcpNoInf=fvReinvestMIRRNoinf-fvCCPS
        Result_spider["Inverter lifespan"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Inverter lifespan"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Inverter lifespan"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Inverter lifespan"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Inverter lifespan"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Inverter lifespan"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Inverter lifespan"]["Sensitivity analysis Cost per KWh"].append(cost_per_kwh)
        Result_spider["Inverter lifespan"]["Sensitivity analysis Future value (IRR rate)"].append(fvReinvestIRR)
        Result_spider["Inverter lifespan"]["Sensitivity analysis Future value (MIRR rate)"].append(fvReinvestMIRR)
        Result_spider["Inverter lifespan"]["Sensitivity analysis Future value (IRR Non-inflated rate)"].append(fvReinvestIRRNoinf)
        Result_spider["Inverter lifespan"]["Sensitivity analysis Future value (MIRR Non-inflated rate)"].append(fvReinvestMIRRNoinf)
        Result_spider["Inverter lifespan"]["Non-inflated IRR"].append(irrNinf)
        Result_spider["Inverter lifespan"]["Non-inflated MIRR"].append(mirrNinf)
        Result_spider["Inverter lifespan"]["Future value IRR-Cost of equity (inflated)"].append(dfvIrrCcpInf)
        Result_spider["Inverter lifespan"]["Future value IRR-Cost of equity (Non-inflated)"].append(dfvIrrCcpNoInf)
        Result_spider["Inverter lifespan"]["Future value MIRR-Cost of equity (inflated)"].append(dfvMirrCcpInf)
        Result_spider["Inverter lifespan"]["Future value MIRR-Cost of equity (Non-inflated)"].append(dfvMirrCcpNoInf)
        #plifespan
        plifespanSpider=int(obj["plifespan"])+int(obj["plifespan"]*percentage)
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"],obj["sellOrComp"],obj["npanel"])
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,plifespanSpider,obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],plifespanSpider,obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,plifespanSpider)
        
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,plifespanSpider,obj["sellOrComp"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        mirrNinf,irrNinf,npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,plifespanSpider,array_cashflow_negative,array_KWhenergy_per_year)
        #ccpSInf=obj["ccp"]+obj["inflation"]+(obj["ccp"]*obj["inflation"])
        fvCCPS=np.fv(obj["ccp"],plifespanSpider, 0,-total_initial_investment[0])
        fvCCPSinf=fvCCPS        
        if irr=="nan" or irrNinf=="nan":
            print(irr)
            print(array_total_cashflow_inflation)
            Irrbolean=True

        pb=Snumath.FinancialSimulation(result_wacc_no_inflation,plifespanSpider,npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation)
        if Irrbolean:
            fvReinvestIRR="nan"
            fvReinvestIRRNoinf="nan"
            dfvIrrCcpInf="nan"
            dfvIrrCcpNoInf="nan"
            irrNinf="nan"
        else:
            fvReinvestIRR=np.fv(irr, plifespanSpider, 0,-total_initial_investment[0])
            fvReinvestIRRNoinf=np.fv(irrNinf, plifespanSpider, 0,-total_initial_investment[0])
            dfvIrrCcpInf=fvReinvestIRR-fvCCPSinf
            dfvIrrCcpNoInf=fvReinvestIRRNoinf-fvCCPS

        
        fvReinvestMIRR=np.fv(mirr, plifespanSpider, 0,-total_initial_investment[0])
        fvReinvestMIRRNoinf=np.fv(mirrNinf, plifespanSpider, 0,-total_initial_investment[0])

        dfvMirrCcpInf=fvReinvestMIRR-fvCCPSinf
        dfvMirrCcpNoInf=fvReinvestMIRRNoinf-fvCCPS
        Result_spider["Panel lifespan"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Panel lifespan"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Panel lifespan"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Panel lifespan"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Panel lifespan"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Panel lifespan"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Panel lifespan"]["Sensitivity analysis Cost per KWh"].append(cost_per_kwh)
        Result_spider["Panel lifespan"]["Sensitivity analysis Future value (IRR rate)"].append(fvReinvestIRR)
        Result_spider["Panel lifespan"]["Sensitivity analysis Future value (MIRR rate)"].append(fvReinvestMIRR)
        Result_spider["Panel lifespan"]["Sensitivity analysis Future value (IRR Non-inflated rate)"].append(fvReinvestIRRNoinf)
        Result_spider["Panel lifespan"]["Sensitivity analysis Future value (MIRR Non-inflated rate)"].append(fvReinvestMIRRNoinf)
        Result_spider["Panel lifespan"]["Non-inflated IRR"].append(irrNinf)
        Result_spider["Panel lifespan"]["Non-inflated MIRR"].append(mirrNinf)
        Result_spider["Panel lifespan"]["Future value IRR-Cost of equity (inflated)"].append(dfvIrrCcpInf)
        Result_spider["Panel lifespan"]["Future value IRR-Cost of equity (Non-inflated)"].append(dfvIrrCcpNoInf)
        Result_spider["Panel lifespan"]["Future value MIRR-Cost of equity (inflated)"].append(dfvMirrCcpInf)
        Result_spider["Panel lifespan"]["Future value MIRR-Cost of equity (Non-inflated)"].append(dfvMirrCcpNoInf)
        #investment
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"],obj["sellOrComp"],obj["npanel"])
        invest_painelsS=invest_painels+(invest_painels*percentage)
        priceinvertersS=obj["priceinverters"]+(obj["priceinverters"]*percentage)
        pricestringboxS=obj["pricestringbox"]+(obj["pricestringbox"]*percentage)
        priceprojectS=obj["priceproject"]+(obj["priceproject"]*percentage)
        pricewiringS=obj["pricewiring"]+(obj["pricewiring"]*percentage)
        pricessS=obj["pricess"]+(obj["pricess"]*percentage)
        pricelaborS=obj["pricelabor"]+(obj["pricelabor"]*percentage)
        priceothersS=obj["priceothers"]+(obj["priceothers"]*percentage)
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painelsS,priceinvertersS,pricestringboxS,priceprojectS,pricewiringS,pricessS,pricelaborS,priceothersS,obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"],obj["sellOrComp"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        mirrNinf,irrNinf,npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year,obj["cct"])
        
        #ccpSInf=obj["ccp"]+obj["inflation"]+(obj["ccp"]*obj["inflation"])
        fvCCPS=np.fv(obj["ccp"],obj["plifespan"], 0,-total_initial_investment[0])
        fvCCPSinf=fvCCPS
        
        if irr=="nan" or irrNinf=="nan":
            print(irr)
            print(array_total_cashflow_inflation)
            Irrbolean=True

        pb=Snumath.FinancialSimulation(result_wacc_no_inflation,obj["plifespan"],npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation)
        if Irrbolean:
            fvReinvestIRR="nan"
            fvReinvestIRRNoinf="nan"
            dfvIrrCcpInf="nan"
            dfvIrrCcpNoInf="nan"
            irrNinf="nan"
        else:
            fvReinvestIRR=np.fv(irr, obj["plifespan"], 0,-total_initial_investment[0])
            fvReinvestIRRNoinf=np.fv(irrNinf, obj["plifespan"], 0,-total_initial_investment[0])
            dfvIrrCcpInf=fvReinvestIRR-fvCCPSinf
            dfvIrrCcpNoInf=fvReinvestIRRNoinf-fvCCPS

        
        fvReinvestMIRR=np.fv(mirr, obj["plifespan"], 0,-total_initial_investment[0])
        fvReinvestMIRRNoinf=np.fv(mirrNinf, obj["plifespan"], 0,-total_initial_investment[0])

        dfvMirrCcpInf=fvReinvestMIRR-fvCCPSinf
        dfvMirrCcpNoInf=fvReinvestMIRRNoinf-fvCCPS

        Result_spider["System price"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["System price"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["System price"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["System price"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["System price"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["System price"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["System price"]["Sensitivity analysis Cost per KWh"].append(cost_per_kwh)
        Result_spider["System price"]["Sensitivity analysis Future value (IRR rate)"].append(fvReinvestIRR)
        Result_spider["System price"]["Sensitivity analysis Future value (MIRR rate)"].append(fvReinvestMIRR)
        Result_spider["System price"]["Sensitivity analysis Future value (IRR Non-inflated rate)"].append(fvReinvestIRRNoinf)
        Result_spider["System price"]["Sensitivity analysis Future value (MIRR Non-inflated rate)"].append(fvReinvestMIRRNoinf)
        Result_spider["System price"]["Non-inflated IRR"].append(irrNinf)
        Result_spider["System price"]["Non-inflated MIRR"].append(mirrNinf)
        Result_spider["System price"]["Future value IRR-Cost of equity (inflated)"].append(dfvIrrCcpInf)
        Result_spider["System price"]["Future value IRR-Cost of equity (Non-inflated)"].append(dfvIrrCcpNoInf)
        Result_spider["System price"]["Future value MIRR-Cost of equity (inflated)"].append(dfvMirrCcpInf)
        Result_spider["System price"]["Future value MIRR-Cost of equity (Non-inflated)"].append(dfvMirrCcpNoInf)
        #wacc
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"],obj["sellOrComp"],obj["npanel"])
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc=result_wacc+(result_wacc*percentage)
        cctSS=obj["cct"]+(obj["cct"]*percentage)
        ccpSS=obj["cct"]+(obj["cct"]*percentage)
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_no_inflation=result_wacc_no_inflation+(result_wacc_no_inflation*percentage)
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"],obj["sellOrComp"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        mirrNinf,irrNinf,npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,ccpSS,array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year,cctSS)
        #ccpSInf=obj["ccp"]+obj["inflation"]+(obj["ccp"]*obj["inflation"])
        fvCCPS=np.fv(ccpSS,obj["plifespan"], 0,-total_initial_investment[0])
        fvCCPSinf=fvCCPS
        
        if irr=="nan" or irrNinf=="nan":
            print(irr)
            print(array_total_cashflow_inflation)
            Irrbolean=True

        pb=Snumath.FinancialSimulation(result_wacc_no_inflation,obj["plifespan"],npv,array_cashflow_negative,array_KWhenergy_per_year,result_wacc,array_total_cashflow_inflation)
        if Irrbolean:
            fvReinvestIRR="nan"
            fvReinvestIRRNoinf="nan"
            dfvIrrCcpInf="nan"
            dfvIrrCcpNoInf="nan"
            irrNinf="nan"
        else:
            fvReinvestIRR=np.fv(irr, obj["plifespan"], 0,-total_initial_investment[0])
            fvReinvestIRRNoinf=np.fv(irrNinf, obj["plifespan"], 0,-total_initial_investment[0])
            dfvIrrCcpInf=fvReinvestIRR-fvCCPSinf
            dfvIrrCcpNoInf=fvReinvestIRRNoinf-fvCCPS

        
        fvReinvestMIRR=np.fv(mirr, obj["plifespan"], 0,-total_initial_investment[0])
        fvReinvestMIRRNoinf=np.fv(mirrNinf, obj["plifespan"], 0,-total_initial_investment[0])

        dfvMirrCcpInf=fvReinvestMIRR-fvCCPSinf
        dfvMirrCcpNoInf=fvReinvestMIRRNoinf-fvCCPS
        Result_spider["Wacc"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Wacc"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Wacc"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Wacc"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Wacc"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Wacc"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Wacc"]["Sensitivity analysis Cost per KWh"].append(cost_per_kwh)
        Result_spider["Wacc"]["Sensitivity analysis Future value (IRR rate)"].append(fvReinvestIRR)
        Result_spider["Wacc"]["Sensitivity analysis Future value (MIRR rate)"].append(fvReinvestMIRR)
        Result_spider["Wacc"]["Sensitivity analysis Future value (IRR Non-inflated rate)"].append(fvReinvestIRRNoinf)
        Result_spider["Wacc"]["Sensitivity analysis Future value (MIRR Non-inflated rate)"].append(fvReinvestMIRRNoinf)
        Result_spider["Wacc"]["Non-inflated IRR"].append(irrNinf)
        Result_spider["Wacc"]["Non-inflated MIRR"].append(mirrNinf)
        Result_spider["Wacc"]["Future value IRR-Cost of equity (inflated)"].append(dfvIrrCcpInf)
        Result_spider["Wacc"]["Future value IRR-Cost of equity (Non-inflated)"].append(dfvIrrCcpNoInf)
        Result_spider["Wacc"]["Future value MIRR-Cost of equity (inflated)"].append(dfvMirrCcpInf)
        Result_spider["Wacc"]["Future value MIRR-Cost of equity (Non-inflated)"].append(dfvMirrCcpNoInf)
        Result_spider["rangeSpider"]=[x/100 for x in rangeSpider]
    if Irrbolean==True:
        Result_spider["IRRflag"]="True"
    else:
        Result_spider["IRRflag"]="False"
    return Result_spider


