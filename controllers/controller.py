from app import app
from flask import render_template
from models.shop_orders import shop_orders



@app.route('/')
def index():
    return render_template("index.html", title="shop_orders", shop_orders=shop_orders)

@app.route('/orders/<index>')
def orders(index):
    return render_template("order.html",  title=index, shop_orders=shop_orders)