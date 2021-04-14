from app import app
from flask import render_template
from models.shop_orders import shop_orders



@app.route('/orders')
def index():
    return render_template("index.html", title="shop_orders", shop_orders=shop_orders)

@app.route('/orders/<index>')
def order(index):
    chosen_order = shop_orders[int(index)]
    return render_template("order.html",  order=chosen_order)