 Multi-Plan TelecommunicationsINPUT:
    User data usage, call minutes, SMS count
    Minimum validity and maximum budget
    List of available plans

eligible_plans = []

FOR each plan:
    IF plan validity < required validity:
        CONTINUE

    Calculate excess data, calls, and SMS

    total_cost = plan price
               + data excess charges
               + call excess charges
               + SMS excess charges
               + other fees
               - discounts

    IF total_cost > budget:
        CONTINUE

    IF plan fails any mandatory usage constraint:
        CONTINUE

    Add plan and total_cost to eligible_plans

IF eligible_plans is empty:
    Report that no plan satisfies all constraints
ELSE:
    Sort by:
        1. Total cost ascending
        2. Cost per validity day ascending
        3. Higher included data allowance
    Recommend the first plan

OUTPUT:
    Cost breakdown for every plan
    Eligible and ineligible plans
    Cheapest eligible plan
    Savings compared with alternatives Optimization: Evaluate several mobile plans against usage, validity, and budget constraints; calculate excess charges and identify the most economical eligible plan. 
