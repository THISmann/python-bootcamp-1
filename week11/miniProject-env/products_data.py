from flask import Flask, render_template
import json


def retrieve_all_products():
    with open('product.json', 'r') as f:
        all_products = json.load(f)
    return render_template('product.html', data=all_products)


def retrieve_requested_product(id):
