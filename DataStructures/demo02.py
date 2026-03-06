
products = [
    {"name":"p1","price":20,"sellingPrice":30},
    {"name":"p2","price":40,"sellingPrice":56},
    {"name":"p3","price":55,"sellingPrice":65},
    {"name": "p4", "price": 55,"sellingPrice":80},
    {"name": "p5", "price": 55,"sellingPrice":100}
]

print(products)
print(len(products))
print(products[2]["price"])

# print(products[0]["name"])
# print(products[1]["name"])
# print(products[2]["name"])

# printing products names with profits
for x in range(len(products)):
    print(products[x]["name"]+" "+str(products[x]["sellingPrice"]-products[x]["price"]))


# calculating total profit
sum = 0
for product in products:
   sum = sum+product["sellingPrice"]-product["price"]

print("total profit:"+str(sum))