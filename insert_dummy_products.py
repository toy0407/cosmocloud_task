from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce_db']
products_collection = db['products']

dummy_products = [
    {
        "name": "LG TV",
        "price": 50000.0,
        "available_quantity": 13
    },
    {
        "name": "Samsung TV",
        "price": 60000.0,
        "available_quantity": 15
    },
    {
        "name": "Macbook Air",
        "price": 120000.0,
        "available_quantity": 20
    },
    {
        "name": "Macbook Pro",
        "price": 160000.0,
        "available_quantity": 12
    },
    {
        "name": "iPhone",
        "price": 100000.0,
        "available_quantity": 10
    },
    {
        "name": "Sony TV",
        "price": 50000.0,
        "available_quantity": 13
    },
    {
        "name": "Lenovo Laptop",
        "price": 170000.0,
        "available_quantity": 15
    },
    {
        "name": "iPad",
        "price": 80000.0,
        "available_quantity": 20
    },
    {
        "name": "Airpods",
        "price": 20000.0,
        "available_quantity": 12
    },
    {
        "name": "Samsung Phone",
        "price": 80000.0,
        "available_quantity": 10
    },
]

# Insert dummy products into MongoDB
for product in dummy_products:
    products_collection.insert_one(product)

print('Products added successfully')

