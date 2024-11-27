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
