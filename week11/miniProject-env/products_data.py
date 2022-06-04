# from flask import Flask, render_template
import json


def retrieve_all_products():
    all_product = 'products.json'
    with open(all_product, 'r') as file:
        datas = json.load(file)
        return datas


def retrieve_requested_product(id):
    datas = retrieve_all_products()
    for data in datas:
        if data['ProductId'] == id:
            return data


# datas = retrieve_all_products()
# print(datas)

data = retrieve_requested_product('HT-1000')
print(data)
