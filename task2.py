INPUT:
    Monthly consumption records
    Slab limits and rates
    Fixed charge
    Surcharge rate
    Rebate rules
    Unusual increase threshold

FOR each month:
    Validate consumption and tariff inputs

    Calculate energy charge using progressive slabs
    Calculate fixed charge
    Calculate surcharge
    Calculate eligible rebate

    Total bill = energy charge
                + fixed charge
                + surcharge
                - rebate

    Store monthly bill and consumption

FOR each month after the first:
    Change = current bill - previous bill

    IF previous bill > 0:
        Percentage change = Change / previous bill * 100
    ELSE:
        Handle zero baseline separately

    IF Percentage change > threshold:
        Flag unusual increase

OUTPUT:
    Monthly bills
    Month-to-month comparison
    Percentage changes
    Unusual increase alerts
