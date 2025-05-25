from ecommerce.pricing import calculate_discount, calculate_tax
from ecommerce.order import generate_order_id, calculate_total

price = 1000
discount_percent = 10
tax_percent = 8

discounted_price = calculate_discount(price, discount_percent)
tax_amount = calculate_tax(discounted_price, tax_percent)
total_amount = calculate_total(price, discount_percent, tax_percent)
order_id = generate_order_id()

print("Your Order ID: ", order_id)
print("Original Price: ", price)
print("Price after discount: ", round(discounted_price, 2))
print("Tax: ", round(tax_amount, 2))
print("Total amount: ", round(total_amount, 2))