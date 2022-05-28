from flask import Flask, render_template, request
import secrets
from db_handler import *
from forms import GoodsFormClass


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)


@app.route('/warehouse', methods=['POST', 'GET'])
def warehouse():
    print(f'Request: {request}')
    title = 'Warehouse'
    info = None
    form = GoodsFormClass()
    print(f'Form Validation: {form.validate_on_submit()}')
    if form.validate_on_submit():
        brand = form.brand.data
        color = form.color.data
        price = form.price.data
        size = form.size.data
        print(f'Brand: {brand} Price: {price} Color: {color}, Size: {size}')
        form = GoodsFormClass(formdata=None)
        info = ['[SAVED]', f'Brand: {brand.upper()}', f'Price: {price}', f'Color: {color.upper()}',
                f'Size: {size.upper()}']
        goods_to_insert = {'Brand': brand,
                          'Price': price,
                          'Color': color,
                          'Size': size
                           }
        res = goods.insert_one(goods_to_insert)
    return render_template('index.html', info=info, form=form, title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
