class Product:
    def __init__(self, product_name, unit_price, gst, quantity):
        self.product_name = product_name
        self.unit_price = unit_price
        self.gst = gst
        self.quantity = quantity

basket = [
    Product("Leather wallet", 1100, 18, 1),
    Product("umbrella", 900, 12, 4),
    Product("cigratte", 200, 28, 3),
    Product("honey", 100, 0, 2)
]

# paid max of gst amount
max_gst_product = None
max_gst_amount = 0
for product in basket:
    gst_amount = product.unit_price * product.gst / 100 * product.quantity
    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = product

print("Product with maximum GST amount:", max_gst_product.product_name)
#print("Maximum GST amount paid:", max_gst_amount)

# total amount here
total_amount = 0
for product in basket:
    if product.unit_price >= 500:
        discount = product.unit_price * 5 / 100
        product.unit_price -= discount

    total_amount += product.unit_price * product.quantity

print("Total amount to be paid:", total_amount)
