from statsmodels.tsa.arima.model import ARIMAResults
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from flask import Flask, render_template
from datetime import datetime
# a single comment
app = Flask(__name__)
model = SARIMAXResults.load('ARIMA_model.pkl')

@app.route('/')
def home():
    # Return the components to the HTML template
    return render_template(
        'chart.html'
    )


@app.route('/predict/<time_stamp>')
def predict(time_stamp):
    index = 14330+int((int(time_stamp)-1679476300398)/1000)
    return str(model.predict(start=index, end=index).tolist()[0])

if __name__ == "__main__":
    # Load dataset from CSV file
    app.run(debug=True, host='0.0.0.0')

