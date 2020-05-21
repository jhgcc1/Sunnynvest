import Snumath

def spiderS(obj):
    Irrbolean=False
    Result_spider={"Energy production":{"Sensitivity analysis LCOE":[],"Sensitivity analysis Cost/KWh":[],"Sensitivity analysis Equivalent annual annuity":[],"Sensitivity analysis Simple Payback":[],"Sensitivity analysis IRR":[],"Sensitivity analysis NPV":[],"Sensitivity analysis MIRR":[]},"Wacc":{"Sensitivity analysis LCOE":[],"Sensitivity analysis Cost/KWh":[],"Sensitivity analysis Equivalent annual annuity":[],"Sensitivity analysis Simple Payback":[],"Sensitivity analysis IRR":[],"Sensitivity analysis NPV":[],"Sensitivity analysis MIRR":[]},"Maintenance":{"Sensitivity analysis LCOE":[],"Sensitivity analysis Cost/KWh":[],"Sensitivity analysis Equivalent annual annuity":[],"Sensitivity analysis Simple Payback":[],"Sensitivity analysis IRR":[],"Sensitivity analysis NPV":[],"Sensitivity analysis MIRR":[]},"System price":{"Sensitivity analysis LCOE":[],"Sensitivity analysis Cost/KWh":[],"Sensitivity analysis Equivalent annual annuity":[],"Sensitivity analysis Simple Payback":[],"Sensitivity analysis IRR":[],"Sensitivity analysis NPV":[],"Sensitivity analysis MIRR":[]}}
    rangeSpider=[x for x in range(-50,50,3)]
    label_year,label_year_simulation,year = Snumath.lebals_years(obj["plifespan"],obj["sim_year"])
    for percent in rangeSpider:
        percentage = percent/100
        #energy
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"])
        kwplantpower=kwplantpower+(kwplantpower*percentage)
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year)
        if irr=="nan":
            Irrbolean=True
        Result_spider["Energy production"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Energy production"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Energy production"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Energy production"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Energy production"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Energy production"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Energy production"]["Sensitivity analysis Cost/KWh"].append(cost_per_kwh)
        
        #maintenance
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"])
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        array_maintenance=array_maintenance+(array_maintenance*percentage)
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year)
        if irr=="nan":
            Irrbolean=True
        Result_spider["Maintenance"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Maintenance"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Maintenance"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Maintenance"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Maintenance"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Maintenance"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Maintenance"]["Sensitivity analysis Cost/KWh"].append(cost_per_kwh)
        #investment
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"])
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
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year)
        if irr=="nan":
            Irrbolean=True
        Result_spider["System price"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["System price"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["System price"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["System price"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["System price"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["System price"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["System price"]["Sensitivity analysis Cost/KWh"].append(cost_per_kwh)
        #wacc
        ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(obj["energyconsume"],obj["economy"],obj["Irradiation"],obj["painelpower"],obj["pricepainel"])
        result_wacc=Snumath.wacc(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["inflation"],obj["profittax"])
        result_wacc=result_wacc+(result_wacc*percentage)
        result_wacc_no_inflation=Snumath.wacc_no_inflation(obj["person_or_business_or_sellenergy"],obj["ccp"],obj["cct"],obj["pccp"],obj["pcct"],obj["profittax"])
        result_wacc_no_inflation=result_wacc_no_inflation+(result_wacc_no_inflation*percentage)
        result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
        array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,obj["plifespan"],obj["pricekwh"],wplantpower,mwplantpower,kwplantpower,obj["initial_pefficiency"],obj["Irradiation"],obj["preduction"],obj["energy_production_tax"])
        total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,obj["priceinverters"],obj["pricestringbox"],obj["priceproject"],obj["pricewiring"],obj["pricess"],obj["pricelabor"],obj["priceothers"],obj["sim_year"],obj["depreciation_years_painels"],obj["depreciation_percentage_inverters"],obj["depreciation_percentage_painels"],year,obj["ilifespan"],obj["plifespan"],obj["depreciation_years_inverters"])
        array_maintenance=Snumath.maintenanceF(obj["maintenance"],ndeplacas,obj["plifespan"])
        total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,obj["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,obj["profittax"],array_maintenance,obj["plifespan"])
        array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(obj["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
        npv,irr,mirr,spayback,vul,cost_per_kwh,lcoe=Snumath.FinancialKPI_spider_and_simulation(result_wacc,array_total_cashflow_inflation,obj["ccp"],array_total_cashflow_noinflation,result_wacc_no_inflation,obj["plifespan"],array_cashflow_negative,array_KWhenergy_per_year)
        if irr=="nan":
            Irrbolean=True
        Result_spider["Wacc"]["Sensitivity analysis IRR"].append(irr)
        Result_spider["Wacc"]["Sensitivity analysis NPV"].append(npv)
        Result_spider["Wacc"]["Sensitivity analysis MIRR"].append(mirr)
        Result_spider["Wacc"]["Sensitivity analysis Simple Payback"].append(spayback)
        Result_spider["Wacc"]["Sensitivity analysis Equivalent annual annuity"].append(vul)
        Result_spider["Wacc"]["Sensitivity analysis LCOE"].append(lcoe)
        Result_spider["Wacc"]["Sensitivity analysis Cost/KWh"].append(cost_per_kwh)
        Result_spider["rangeSpider"]=[x/100 for x in rangeSpider]
    if Irrbolean==True:
        Result_spider["IRRflag"]=True
    return Result_spider


