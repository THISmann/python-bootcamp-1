# from flask import Flask, render_template
import json


def retrieve_all_products():
    all_product = 'product.json'
    with open(all_product, 'r') as file:
        datas = json.load(all_product)
        print(datas)

    retrieve_all_products()

# def retrieve_requested_product():
#     data = retrieve_all_products()
#     print(data)
#     for i in data.keys():
#         print(i)

#     datas = retrieve_requested_product()
#     print(datas)
