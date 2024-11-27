from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Factory Management System API',
          description='API for managing factory operations.')

# Namespaces
product_ns = api.namespace('products', description='Product operations')
order_ns = api.namespace('orders', description='Order operations')
customer_ns = api.namespace('customers', description='Customer operations')
production_ns = api.namespace('production', description='Production operations')

# Define Product Model
product_model = api.model('Product', {
    'id': fields.Integer(description='Product ID', example=1),
    'name': fields.String(required=True, description='Name of the product', example='Widget A'),
    'price': fields.Float(required=True, description='Price of the product', example=15.99),
    'stock': fields.Integer(required=True, description='Stock quantity', example=100)
})

@product_ns.route('/')
class ProductList(Resource):
    @api.doc('list_products')
    @api.marshal_list_with(product_model)
    def get(self):
        """List all products"""
        return [
            {"id": 1, "name": "Widget A", "price": 15.99, "stock": 100},
            {"id": 2, "name": "Gadget B", "price": 9.99, "stock": 200}
        ]

    @api.doc('create_product')
    @api.expect(product_model)
    @api.response(201, 'Product successfully created.')
    def post(self):
        """Create a new product"""
        data = request.json
        return {"message": "Product created successfully", "product": data}, 201

# Define Order Model
order_model = api.model('Order', {
    'id': fields.Integer(description='Order ID', example=1),
    'product_id': fields.Integer(required=True, description='Product ID', example=1),
    'quantity': fields.Integer(required=True, description='Quantity ordered', example=10),
    'customer_id': fields.Integer(required=True, description='Customer ID', example=1),
    'status': fields.String(description='Order status', example='Pending')
})

@order_ns.route('/')
class OrderList(Resource):
    @api.doc('list_orders')
    @api.marshal_list_with(order_model)
    def get(self):
        """List all orders"""
        return [
            {"id": 1, "product_id": 1, "quantity": 10, "customer_id": 1, "status": "Completed"},
            {"id": 2, "product_id": 2, "quantity": 5, "customer_id": 2, "status": "Pending"}
        ]

    @api.doc('create_order')
    @api.expect(order_model)
    @api.response(201, 'Order successfully created.')
    def post(self):
        """Create a new order"""
        data = request.json
        return {"message": "Order created successfully", "order": data}, 201

# Define Customer Model
customer_model = api.model('Customer', {
    'id': fields.Integer(description='Customer ID', example=1),
    'name': fields.String(required=True, description='Full name of the customer', example='Alice Green'),
    'email': fields.String(required=True, description='Email address', example='alice@example.com'),
    'phone': fields.String(description='Phone number', example='+1234567890')
})

@customer_ns.route('/')
class CustomerList(Resource):
    @api.doc('list_customers')
    @api.marshal_list_with(customer_model)
    def get(self):
        """List all customers"""
        return [
            {"id": 1, "name": "Alice Green", "email": "alice@example.com", "phone": "+1234567890"},
            {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "phone": "+9876543210"}
        ]

    @api.doc('create_customer')
    @api.expect(customer_model)
    @api.response(201, 'Customer successfully created.')
    def post(self):
        """Create a new customer"""
        data = request.json
        return {"message": "Customer created successfully", "customer": data}, 201

# Define Production Model
production_model = api.model('Production', {
    'id': fields.Integer(description='Production ID', example=1),
    'product_id': fields.Integer(required=True, description='Product ID being produced', example=1),
    'quantity': fields.Integer(required=True, description='Quantity produced', example=50),
    'status': fields.String(description='Production status', example='In Progress'),
    'timestamp': fields.String(description='Production timestamp', example='2024-11-25T12:00:00Z')
})

@production_ns.route('/')
class ProductionList(Resource):
    @api.doc('list_productions')
    @api.marshal_list_with(production_model)
    def get(self):
        """List all production records"""
        return [
            {"id": 1, "product_id": 1, "quantity": 50, "status": "Completed", "timestamp": "2024-11-25T12:00:00Z"},
            {"id": 2, "product_id": 2, "quantity": 30, "status": "In Progress", "timestamp": "2024-11-25T14:00:00Z"}
        ]

    @api.doc('create_production')
    @api.expect(production_model)
    @api.response(201, 'Production record successfully created.')
    def post(self):
        """Create a new production record"""
        data = request.json
        return {"message": "Production record created successfully", "production": data}, 201

@product_ns.route('/')
class ProductList(Resource):
    @api.doc('list_products')
    @api.marshal_list_with(product_model)
    @api.response(200, 'Successful response', [
        {"id": 1, "name": "Widget A", "price": 15.99, "stock": 100},
        {"id": 2, "name": "Gadget B", "price": 9.99, "stock": 200}
    ])
    def get(self):
        """List all products"""
        return [
            {"id": 1, "name": "Widget A", "price": 15.99, "stock": 100},
            {"id": 2, "name": "Gadget B", "price": 9.99, "stock": 200}
        ]

    @api.doc('create_product')
    @api.expect(product_model)
    @api.response(201, 'Product successfully created', {
        "id": 3,
        "name": "New Product",
        "price": 20.99,
        "stock": 50
    })
    def post(self):
        """Create a new product"""
        data = request.json
        return {"message": "Product created successfully", "product": data}, 201

@order_ns.route('/')
class OrderList(Resource):
    @api.doc('list_orders')
    @api.marshal_list_with(order_model)
    @api.response(200, 'Successful response', [
        {"id": 1, "product_id": 1, "quantity": 10, "customer_id": 1, "status": "Completed"},
        {"id": 2, "product_id": 2, "quantity": 5, "customer_id": 2, "status": "Pending"}
    ])
    def get(self):
        """List all orders"""
        return [
            {"id": 1, "product_id": 1, "quantity": 10, "customer_id": 1, "status": "Completed"},
            {"id": 2, "product_id": 2, "quantity": 5, "customer_id": 2, "status": "Pending"}
        ]

    @api.doc('create_order')
    @api.expect(order_model)
    @api.response(201, 'Order successfully created', {
        "id": 3,
        "product_id": 1,
        "quantity": 20,
        "customer_id": 3,
        "status": "Pending"
    })
    def post(self):
        """Create a new order"""
        data = request.json
        return {"message": "Order created successfully", "order": data}, 201

@customer_ns.route('/')
class CustomerList(Resource):
    @api.doc('list_customers')
    @api.marshal_list_with(customer_model)
    @api.response(200, 'Successful response', [
        {"id": 1, "name": "Alice Green", "email": "alice@example.com", "phone": "+1234567890"},
        {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "phone": "+9876543210"}
    ])
    def get(self):
        """List all customers"""
        return [
            {"id": 1, "name": "Alice Green", "email": "alice@example.com", "phone": "+1234567890"},
            {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "phone": "+9876543210"}
        ]

    @api.doc('create_customer')
    @api.expect(customer_model)
    @api.response(201, 'Customer successfully created', {
        "id": 3,
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "+1122334455"
    })
    def post(self):
        """Create a new customer"""
        data = request.json
        return {"message": "Customer created successfully", "customer": data}, 201

@production_ns.route('/')
class ProductionList(Resource):
    @api.doc('list_productions')
    @api.marshal_list_with(production_model)
    @api.response(200, 'Successful response', [
        {"id": 1, "product_id": 1, "quantity": 50, "status": "Completed", "timestamp": "2024-11-25T12:00:00Z"},
        {"id": 2, "product_id": 2, "quantity": 30, "status": "In Progress", "timestamp": "2024-11-25T14:00:00Z"}
    ])
    def get(self):
        """List all production records"""
        return [
            {"id": 1, "product_id": 1, "quantity": 50, "status": "Completed", "timestamp": "2024-11-25T12:00:00Z"},
            {"id": 2, "product_id": 2, "quantity": 30, "status": "In Progress", "timestamp": "2024-11-25T14:00:00Z"}
        ]

    @api.doc('create_production')
    @api.expect(production_model)
    @api.response(201, 'Production record successfully created', {
        "id": 3,
        "product_id": 3,
        "quantity": 25,
        "status": "In Progress",
        "timestamp": "2024-11-26T10:00:00Z"
    })
    def post(self):
        """Create a new production record"""
        data = request.json
        return {"message": "Production record created successfully", "production": data}, 201

if __name__ == '__main__':
    app.run(debug=True) 
    
    # For Swagger UI: http://localhost:5000/apidocs/
    # For testing API endpoints: http://localhost:5000/api/v1/
    # For testing API endpoints: http://localhost:5000/api/v1/products
    # For testing API endpoints: http://localhost:5000/api/v1/orders
    # For testing API endpoints: http://localhost:5000/api/v1/customers
    # For testing API endpoints: http://localhost:5000/api/v1/productions
