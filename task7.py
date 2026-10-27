INPUT:
    Household consumption records
    Progressive tariff slabs
    Fixed monthly fee
    Penalty threshold and amount
    Excessive-usage alert threshold

FOR each household:
    Validate consumption

    slab_charge = 0
    remaining = consumption

    FOR each progressive slab:
        units_in_slab = units applicable to this slab
        slab_charge += units_in_slab * slab_rate

    fixed_charge = configured fixed fee

    IF consumption > penalty_threshold:
        penalty = configured penalty
    ELSE:
        penalty = 0

    total_bill = slab_charge + fixed_charge + penalty

    Compare consumption against alert threshold
    Compare consumption against historical records

    Store bill and usage alerts

OUTPUT:
    Household-wise itemized bills
    Total water consumption
    Total revenue
    High-usage alerts
    Month-to-month consumption comparison
