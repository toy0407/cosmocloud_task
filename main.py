from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models.product import Product
from models.order import Order, OrderItem, UserAddress




app = FastAPI()


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce_db']
products_collection = db['products']
orders_collection = db['orders']





# Routes

"""
Task 1: API to list all available products
/products
"""
@app.get("/products")
async def list_products():
    products = list(products_collection.find({},{"_id": False})) 
    return products




