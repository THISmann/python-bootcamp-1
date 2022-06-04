from flask import Flask, render_template
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
    return render_template('product.html', Products=donnees)


@app.route('/products/<product_id>')
def ProductsId(product_id):
    return render_template('product.html', product_id=product_id)
