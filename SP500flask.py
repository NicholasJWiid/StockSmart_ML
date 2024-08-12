from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine, MetaData

# Create a Flask app
app = Flask(__name__)
# Connect to the database
engine = create_engine("postgresql://postgres:password123@localhost/CAGRdata")
metadata = MetaData()

# Reflect the table
metadata.reflect(bind=engine, only=['cagr_data'])

# Get the reflected table
stock_data_table = metadata.tables['cagr_data']

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/tickers')
def get_tickers():
    with engine.connect() as conn:
        query = stock_data_table.select()
        result = conn.execute(query)
        
        # Fetch all rows
        rows = result.fetchall()
        
        # Get column names
        columns = result.keys()
        
        # Convert rows to a list of dictionaries
        tickers = [
            dict(zip(columns, row))
            for row in rows
        ]

    return jsonify(tickers)



@app.route('/data/<ticker>')
def get_data(ticker):
    with engine.connect() as conn:
        query = stock_data_table.select().where(stock_data_table.c.ticker == ticker)
        result = conn.execute(query)
        row = result.fetchone()

    if row is None:
        return jsonify({'error': 'Ticker not found'}), 404

    # Convert row to a dictionary
    row_dict = dict(zip(result.keys(), row))

    cagr_values = [
        row_dict.get('cagr_2015', 0),
        row_dict.get('cagr_2016', 0),
        row_dict.get('cagr_2017', 0),
        row_dict.get('cagr_2018', 0),
        row_dict.get('cagr_2019', 0),
        row_dict.get('cagr_2020', 0),
        row_dict.get('cagr_2021', 0),
        row_dict.get('cagr_2022', 0),
        row_dict.get('cagr_2023', 0)
    ]
    years = list(range(2015, 2024, +1))  # From 2023 to 2015

    # Example S&P 500 CAGR values for demonstration purposes
    sp500_values = [-0.73, 9.84, 18.74, -6.59, 30.43, 15.76, 26.60, -19.64, 23.79]
    interest_rate = [0.13, 0.39, 1, 1.79, 2.16, 0.36, 0.08, 1.68, 5.03]
    cpi = [0.1, 1.3, 2.1, 2.4, 1.8, 1.2, 4.7, 8, 3.2]
    unemployment_rate = [5.3, 4.9, 4.4, 3.9, 3.7, 8.1, 5.4, 3.6, 3.5]
    gdp_growth = [2.9, 1.8, 2.5, 3, 2.5, -2.2, 5.8, 1.9, 2.5]


    return jsonify({
        'stock_name': row_dict.get('stock_name', 'Unknown'),
        'headquarters': row_dict.get('headquarters', 'Unknown'),
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
