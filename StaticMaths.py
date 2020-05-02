import Snumath

def staticMaths(objIpunt):
    label_year,label_year_simulation,year = Snumath.lebals_years(objIpunt["plifespan"],0)
    ndeplacas,invest_painels,maxeconomy,wplantpower,kwplantpower,mwplantpower = Snumath.InitialCalculations(objIpunt["energyconsume"],objIpunt["economy"],objIpunt["Irradiation"],objIpunt["painelpower"],objIpunt["pricepainel"])
    result_wacc=Snumath.wacc(objIpunt["person_or_business_or_sellenergy"],objIpunt["ccp"],objIpunt["cct"],objIpunt["pccp"],objIpunt["pcct"],objIpunt["inflation"],objIpunt["profittax"])
    result_wacc_no_inflation=Snumath.wacc_no_inflation(objIpunt["person_or_business_or_sellenergy"],objIpunt["ccp"],objIpunt["cct"],objIpunt["pccp"],objIpunt["pcct"],objIpunt["profittax"])
    result_wacc_m_no_inflation=Snumath.wacc_m_no_inflation(result_wacc_no_inflation)
    array_gross_revenue,array_Whenergy_per_year,array_KWhenergy_per_year,array_MWhenergy_per_year=Snumath.energyProduction(result_wacc_m_no_inflation,objIpunt["plifespan"],objIpunt["pricekwh"],wplantpower,mwplantpower,kwplantpower,objIpunt["initial_pefficiency"],objIpunt["Irradiation"],objIpunt["preduction"],objIpunt["energy_production_tax"])
    total_initial_investment,array_depreciation_inverters,array_investmentinvertes,array_depreciation_painels,array_residual_value_inverters=Snumath.derepciation_and_investment_and_reinvestment_and_residual_value(invest_painels,objIpunt["priceinverters"],objIpunt["pricestringbox"],objIpunt["priceproject"],objIpunt["pricewiring"],objIpunt["pricess"],objIpunt["pricelabor"],objIpunt["priceothers"],0,objIpunt["depreciation_years_painels"],objIpunt["depreciation_percentage_inverters"],objIpunt["depreciation_percentage_painels"],year,objIpunt["ilifespan"],objIpunt["plifespan"],objIpunt["depreciation_years_inverters"])
    array_maintenance=Snumath.maintenanceF(objIpunt["maintenance"],ndeplacas,objIpunt["plifespan"])
    total_fiscaleffets=Snumath.fiscal_effects(array_gross_revenue,objIpunt["person_or_business_or_sellenergy"],array_depreciation_inverters,array_depreciation_painels,objIpunt["profittax"],array_maintenance,objIpunt["plifespan"])
    array_total_cashflow_noinflation,array_total_cashflow_inflation,array_cashflow_negative=Snumath.cash_flow_no_inflation_and_inflation(objIpunt["inflation"],total_initial_investment,array_maintenance,array_investmentinvertes,array_gross_revenue,array_residual_value_inverters,total_fiscaleffets)
    abcList,array_co2_reduction,sum_array_KWhenergy_per_year,sum_array_gross_revenue,sum_array_gross_revenue_inf,spayback,array_discounted_payback,array_annuity_inflation_cashflow,array_annuity_noinflation_cashflow,annuity_payment_inflation,annuity_payment_noinflation=Snumath.Static(invest_painels,objIpunt["priceinverters"],objIpunt["pricestringbox"],objIpunt["priceproject"],objIpunt["pricewiring"],objIpunt["pricess"],objIpunt["pricelabor"],objIpunt["priceothers"],objIpunt["entry"],objIpunt["carbon_red"],array_KWhenergy_per_year,objIpunt["plifespan"],array_gross_revenue,objIpunt["inflation"],array_total_cashflow_noinflation,result_wacc,array_total_cashflow_inflation,objIpunt["yearsTopay"],result_wacc_no_inflation)
    print("aqui")
    print(total_fiscaleffets)
    resultStatic={"Pareto chart":abcList,
    "Produced KWh per year":array_KWhenergy_per_year.tolist(),
    "CO2 emition reduction":array_co2_reduction.tolist(),
    "Sum of produced KWh per year":sum_array_KWhenergy_per_year.tolist(),
    "Sum of gross revenue without inflation":sum_array_gross_revenue.tolist(),
    "Sum of gross revenue with inflation":sum_array_gross_revenue_inf.tolist(),
    "Simple payback":spayback,
    "Discounted payback":array_discounted_payback.tolist(),
    "Annuity payment with inflation cashflow":array_annuity_inflation_cashflow.tolist(),
    "Annuity payment without inflation cashflow":array_annuity_noinflation_cashflow.tolist(),
    "Annuity payment with inflation":annuity_payment_inflation.tolist(),
    "Annuity payment without inflation":annuity_payment_noinflation.tolist(),
    "Cashflow without inflation":array_total_cashflow_noinflation.tolist(),
    "Cashflow with inflation":array_total_cashflow_inflation.tolist(),
    "Fiscal Effects":total_fiscaleffets.tolist(),
    "Inverters depreciation":array_depreciation_inverters.tolist(),
    "inverters reinvestments":array_investmentinvertes.tolist(),
    "panels depreciation":array_depreciation_painels.tolist(),
    "Maintenance expenses":array_maintenance.tolist(),
    "Years":label_year,
    "paymentMethod":objIpunt["paymentMethod"],
    "ndeplacas":ndeplacas,
    "maxeconomy":maxeconomy}
    return resultStatic