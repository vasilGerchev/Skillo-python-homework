import csv
import json


def read_product_price():
    product_price = {}
    with open('product.json', 'r') as products:
        product_json = json.load(products)
        for product in product_json:
            product_price[product["name"]] = product["price"]

    return product_price


def read_product_sale():
    product_sale = []
    with open('sale.csv') as products:
        reader = csv.reader(products)
        reader.__next__()
        for row in reader:
            date, name, amount = row
            product_sale.append({
                "date": date,
                "name": name,
                "amount": amount
            })

    return product_sale


def calculate_revenue(product_sale, product_price):
    revenue = {}
    for sales in product_sale:
        name = sales["name"]
        product_revenue = float(product_price[name]) * float(sales["amount"])
        if revenue.get(name) is None:
            revenue[name] = product_revenue
        else:
            revenue[name] += product_revenue

    return revenue


product_price = read_product_price()
product_sale = read_product_sale()
revenue = calculate_revenue(product_sale, product_price)

print(product_price)
print(product_sale)
print(revenue)
