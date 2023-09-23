import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException, Query, Request
from pymongo import MongoClient
from models.order import Order

app = FastAPI()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce_db']
products_collection = db['products']
orders_collection = db['orders']

# Routes
"""
Task 1: API to list all available products
GET /products
"""
@app.get("/products")
async def list_products():
    products = list(products_collection.find({},{"_id": False})) # Getting all available products as list
    return products



"""
Task 2: API to create a new order
POST /orders
"""
@app.post("/orders")
async def create_order(order: Order):
    # Calculating the total order value
    total_amount = get_total_amount(order) 

    order_data = order.dict()
    order_data['order_id'] = uuid.uuid4().hex[:8]
    order_data['timestamp'] = datetime.now() 
    order_data['total_amount'] = total_amount

    # Adding the order into the Orders database
    orders_collection.insert_one(order_data)

    return {"message": "Order placed successfully"}



"""
Task 3: API to fetch all orders from the system by pagination using limit and offset.
GET /orders/?page=0&limit=3
Query params:
    page = 0 (default)
    limit = 3 (default)
"""
@app.get("/orders/")
async def list_orders(page: int = 0, limit: int = 3):
    orders = list(orders_collection.find({},{"_id": False}).skip(page).limit(limit))
    return orders



"""
Task 4: API to fetch a single order by Order ID
GET /orders/{order_id}
"""
@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    order = orders_collection.find_one({"order_id": order_id},{"_id":False})
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order



"""
Task 5: API to update a product
PUT /products/{product_id}
"""
@app.put("/products/{product_id}")
async def update_product_quantity(product_id: str, request: Request):
    json_body = await request.json()
    available_quantity = json_body['available_quantity']
    
    if available_quantity is not None:
        products_collection.update_one(
            {"product_id": product_id},
            {"$set": {"available_quantity": available_quantity}}
        )
        return {"message": "Product quantity updated successfully"}
    else:
        raise HTTPException(status_code=400, detail="Quantity not provided in request body")








# Helper functions

# Calculate the total amount for all items in the Order
def get_total_amount(order: Order):

    sum = 0 # Calculate the total amount

    for item in order.items:
        product = products_collection.find_one({"product_id":item.product_id})
        available_quantity = product["available_quantity"]
        if(product is not None):
            if(item.bought_quantity<=available_quantity):
                # If buying quantity <= available quantity, purchase all items and update available quantity
                sum = sum + item.bought_quantity*product["price"]
                products_collection.update_one({"product_id": item.product_id},{"$set": {"available_quantity": available_quantity-item.bought_quantity}})
            else:
                # If buying quantity > available quantity, buy the whole stock and set available quantity to 0
                sum = sum + available_quantity*product["price"]
                products_collection.update_one({"product_id": item.product_id},{"$set": {"available_quantity": 0}})
                item.bought_quantity = available_quantity
    return sum

