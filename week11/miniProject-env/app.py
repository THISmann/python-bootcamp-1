from flask import Flask, render_template,  redirect, url_for
import products_data

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
