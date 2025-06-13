from flask import Flask

# create a new instance of Flask app
app = Flask(__name__)

# routes collection
@app.route('/', methods=['GET'])
def root():
    # returned value will be sent to the client
    return "hello client"


@app.route('/products', methods=['GET'])
def product_list():
    products = [
        {"id": 1, "title":"product1", "price": 100},
        {"id": 2, "title":"product2", "price": 200},
        {"id": 3, "title":"product3", "price": 300},
        {"id": 4, "title":"product4", "price": 400}
    ]
    # sending the list of dictionaries in JSON format to the client
    return products

# start the application
app.run(host="0.0.0.0", port=4000, debug=True)
