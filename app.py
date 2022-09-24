from flask import Flask, request
from utils import get_filtered_customers, get_unique_customers_by_sql, get_sum_of_invoice_items

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><b>Hello, World!</b></p>"


@app.route("/db_find", methods=['GET'])
def db_ST_customer():
    city = request.args.get('city', default = None)
    state = request.args.get('state', default = None)
    result = get_filtered_customers(state=state, city=city)
    return result

@app.route("/db_name", methods=['GET'])
def db_customer_name():
    name = request.args.get('name', default = 'Helena')
    result = get_unique_customers_by_sql(name)
    return result

@app.route("/db_sum_items", methods=['GET'])
def db_items_sum():
    return get_sum_of_invoice_items()