from flask import Flask, render_template, request

app = Flask(__name__)

# Stock prices (you can update these)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "INFY": 1450,
    "GOOGL": 2700,
    "MSFT": 340
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    total = 0

    if request.method == 'POST':
        symbols = request.form.getlist('symbol')
        quantities = request.form.getlist('quantity')

        for symbol, qty in zip(symbols, quantities):
            symbol = symbol.upper()
            if symbol in stock_prices:
                price = stock_prices[symbol]
                value = price * int(qty)
                total += value
                result.append({
                    'symbol': symbol,
                    'price': price,
                    'qty': qty,
                    'value': value
                })

    return render_template('index.html', result=result, total=total)

if __name__ == '__main__':
    app.run(debug=True)
