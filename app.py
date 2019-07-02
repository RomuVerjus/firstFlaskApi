from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': "my shop",
        'items': [
            {
                'name': 'my item',
                'price': 15.99
            }
        ]
    }
]


# @app.route('/')
# def home():
#     return "Hello world"

@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store():
    pass


@app.route('/store')
def get_stores():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass


@app.route('/store/<string:name>/item')
def get_items_in_store():
    pass


app.run(port=5000)
