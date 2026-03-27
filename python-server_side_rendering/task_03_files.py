#!/usr/bin/python3
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filename):
    """Read product data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file(filename):
    """Read product data from a CSV file."""
    products = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error='Product not found')

        filtered = [product for product in data if product.get('id') == product_id]
        if not filtered:
            return render_template('product_display.html', error='Product not found')
        data = filtered

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
