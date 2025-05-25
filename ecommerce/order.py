import uuid

def generate_order_id():

    return str(uuid.uuid4())

def calculate_total(price, discount_percent, tax_percent):
    
    discounted_price = price - (price * discount_percent / 100)
    tax = discounted_price * tax_percent / 100
    total = discounted_price + tax
    return total

