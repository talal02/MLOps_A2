from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from flask import Flask, render_template
from datetime import datetime

regressor = None
labels = []
data = []

app = Flask(__name__)


@app.route('/')
def home():
    # Return the components to the HTML template
    return render_template(
        'chart.html'
    )


@app.route('/predict/<time_stamp>')
def predict(time_stamp):
    time_stamp = float(time_stamp)
    predicted_price = regressor.predict([[time_stamp]])
    print("Predicted price for %0.1f years of experience: $%0.2f" % (time_stamp, predicted_price[0]))
    return str(predicted_price[0])

if __name__ == "__main__":
    # Load dataset from CSV file
    df = pd.read_csv('data.csv')

    # Split data into input and output variables
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)

    # Train linear regression model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predict salaries on test set
    y_pred = regressor.predict(X_test)

    # Print model coefficients and accuracy
    print("Coefficients:", regressor.coef_)
    print("Intercept:", regressor.intercept_)
    print("Accuracy:", regressor.score(X_test, y_test))
    app.run(debug=True, host='0.0.0.0')

