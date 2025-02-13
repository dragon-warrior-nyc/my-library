from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

products = pd.read_csv('data/book.csv').to_dict(orient='records') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    results = [product for product in products if query in product['name'].lower()]
    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)