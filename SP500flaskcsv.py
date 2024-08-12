from flask import Flask, jsonify, render_template, request
import pandas as pd

# Create a Flask app
app = Flask(__name__)

# Load CSV data into a DataFrame
df = pd.read_csv('cagr_data.csv')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/tickers')
def get_tickers():
    # Convert DataFrame to list of dictionaries
    tickers = df.to_dict(orient='records')
    return jsonify(tickers)

@app.route('/data/<ticker>')
def get_data(ticker):
    # Filter DataFrame by ticker
    row = df[df['ticker'] == ticker].iloc[0]

    if row.empty:
        return jsonify({'error': 'Ticker not found'}), 404

    # Extract data
    cagr_values = [
        row.get('cagr_2015', 0),
        row.get('cagr_2016', 0),
        row.get('cagr_2017', 0),
        row.get('cagr_2018', 0),
        row.get('cagr_2019', 0),
        row.get('cagr_2020', 0),
        row.get('cagr_2021', 0),
        row.get('cagr_2022', 0),
        row.get('cagr_2023', 0)
    ]
    years = list(range(2015, 2024))

    # Example values
    sp500_values = [-0.73, 9.84, 18.74, -6.59, 30.43, 15.76, 26.60, -19.64, 23.79]
    interest_rate = [0.13, 0.39, 1, 1.79, 2.16, 0.36, 0.08, 1.68, 5.03]
    cpi = [0.1, 1.3, 2.1, 2.4, 1.8, 1.2, 4.7, 8, 3.2]
    unemployment_rate = [5.3, 4.9, 4.4, 3.9, 3.7, 8.1, 5.4, 3.6, 3.5]
    gdp_growth = [2.9, 1.8, 2.5, 3, 2.5, -2.2, 5.8, 1.9, 2.5]

    return jsonify({
        'stock_name': row.get('stock_name', 'Unknown'),
        'headquarters': row.get('headquarters', 'Unknown'),
        'years': years,
        'cagr': cagr_values,
        'sp500': sp500_values,
        'interest': interest_rate,
        'cpi': cpi,
        'unemployment': unemployment_rate,
        'gdp': gdp_growth
    })

if __name__ == '__main__':
    app.run(debug=True)
