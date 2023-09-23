from datetime import datetime
import uuid
from fastapi import FastAPI, HTTPException, Query, Request
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
GET /products
"""
@app.get("/products")
async def list_products():
    products = list(products_collection.find({},{"_id": False})) 
    return products



"""
Task 2: API to create a new order
POST /orders
"""
@app.post("/orders")
async def create_order(order: Order):

    order_data = order.dict()
    order_data['order_id'] = uuid.uuid4().hex[:8]
    order_data['timestamp'] = datetime.now()
    order_data['total_amount'] = get_total_amount()

    # print(order_data)


    orders_collection.insert_one(order_data)
    return {"message": "Order created successfully"}



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

























def get_total_amount():
    return 100
    # pipeline = [
    #     {
    #         "$lookup": {
    #             "from": "Product",  # Name of the product collection
    #             "localField": "product_id",
    #             "foreignField": "product_id",
    #             "as": "product_data"
    #         }
    #     },
    #     {
    #         "$unwind": "$product_data"
    #     },
    #     {
    #         "$project": {
    #             "amount": {
    #                 "$multiply": [
    #                     {
    #                         "$min": ["$bought_quantity", "$product_data.available_quantity"]
    #                     },
    #                     "$product_data.price"
    #                 ]
    #             }
    #         }
    #     },
    #     {
    #         "$group": {
    #             "_id": None,
    #             "total_amount": {
    #                 "$sum": "$amount"
    #             }
    #         }
    #     }
    # ]

    # result = db.OrderItem.aggregate(pipeline)

    # for doc in result:
    #     print(doc)