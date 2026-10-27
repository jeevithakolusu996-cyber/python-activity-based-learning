INPUT:
    Products, quantities, prices, categories
    Category tax rates
    Threshold discount rules
    Maximum concession limit

gross_total = 0

FOR each item:
    Validate quantity and price
    item_gross = price * quantity
    gross_total += item_gross

eligible_discount = determine_discount(gross_total)
allowed_discount = MIN(eligible_discount, concession_limit)

FOR each item:
    allocated_discount =
        allowed_discount * item_gross / gross_total

    taxable_amount = item_gross - allocated_discount
    item_tax = taxable_amount * category_tax_rate

    Record item gross, discount, taxable amount, and tax

total_tax = SUM(item_tax)
payable = gross_total - allowed_discount + total_tax

OUTPUT:
    Itemized invoice
    Gross subtotal
    Discount and concession cap applied
    Category-wise taxes
    Final payable amount
