INPUT:
    Parcel weight and dimensions
    Destination zone and urgency
    Declared restrictions
    Maximum budget
    Available courier services

volumetric_weight = length * width * height / divisor
chargeable_weight = max(actual_weight, volumetric_weight)

eligible_services = []

FOR each service:
    Check weight and dimension limits
    Check destination coverage
    Check urgency availability
    Check prohibited-item and handling restrictions

    IF any mandatory check fails:
        Record reason for rejection
        CONTINUE

    Calculate base fee
    Calculate weight charge
    Add zone and urgency surcharges
    Add handling fees and taxes

    IF total charge <= budget:
        Add service to eligible_services

IF eligible_services is empty:
    Report no eligible service
ELSE:
    Sort by total charge ascending
    Recommend lowest-cost service
    Report savings against alternatives

OUTPUT:
    Cost breakdown per service
    Eligibility and rejection reasons
    Recommended service
