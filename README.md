# E-Commerce API

This is a simple e-commerce application.

# Setup

1. Install Python.
2. Install MongoDB.
3. Run the following command in terminal: "pip3 install fastapi pymongo uvicorn uuid".
4. Add uvicorn to PATH.
5. Run the file insert_dummy_products.py once.
6. Run the following command in terminal: "uvicorn main:app --reload".

# Endpoints

## 1. List all available products in the system.

    Request Type: GET
    URL: http://localhost:8000/products

## 2. Create a new order

    Request Type: POST
    URL: http://localhost:8000/orders

## 3. Fetch all orders from the system

    Request Type: GET
    URL: http://localhost:8000/orders/?page=0&limit=3

### Query params:

    page = 0 (default)
    limit = 3 (default)

## 4. Fetch single order by OrderID

    Request Type: GET
    URL: http://localhost:8000/orders/{order_id}

## 5. Update available quantity for a product

    Request Type: PUT
    URL: http://localhost:8000/products/{product_id}

# Model Structure

    Product
    |----- product_id: string
    |----- name: string
    |----- price: float
    |----- available_quantity: integer

    Order
    |----- order_id: string
    |----- timestamp: datetime
    |----- total_amount: float
    |----- items: List[OrderItem]
    |----- user_address: UserAddress
                         |----- city: string
                         |----- country: string
                         |----- zip_code: string

    OrderItem
    |----- product_id: string
    |----- bought_quantity: integer
