from flask import Flask, render_template,  redirect, url_for
import products_data
cart_item = []
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=5500)

donnees = products_data.retrieve_all_products()
# print(donnees)


@app.route('/')
def homeUser():
    return render_template('index.html', user="test")


@app.route('/products')
def Product():
    return render_template('products.html', Products=donnees)


@app.route('/products/<product_id>')
def ProductID(product_id):
    return render_template('product.html', Product=products_data.retrieve_requested_product(product_id))


@app.route('/cart')
def cart():
    return render_template('cart.html',  Products=donnees)


@app.route('/delete/<product_id>')
def delete(product_id):
    item = products_data.retrieve_requested_product(product_id)
    index = donnees.index(item)
    del donnees[index]
    # redirect(url_for(cart))
    return render_template('cart.html', prod_id=product_id)


@app.route('/add_product_to_card/<product_id>')
def addProduct(product_id):
    product = products_data.retrieve_requested_product(product_id)
    cart_item.append(product)
    print(cart_item)
    data = tuple(cart_item)
    return data


# @app.route('/delete_product_from_cart/<product_id>')
# def delete(product_id):
#     item = products_data.retrieve_requested_product(product_id)
#     index = cart_item.index(item)
#     del cart_item[index]
#     print(cart_item)


@app.route('/signup')
def add_user():
    return render_template('signup.html', signup={})


@app.route('/login')
def check_user():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('homeUser'))
    
    return render_template('login.html', login={})
