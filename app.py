from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>PredictServe</title>
        </head>
        <body style="font-family: Arial; padding: 40px;">
            <h2>Purchase Prediction</h2>
            <form action="/predict" method="post">
                <label>Age:</label><br>
                <input type="number" name="age" required><br><br>

                <label>Salary:</label><br>
                <input type="number" name="salary" required><br><br>

                <button type="submit">Predict</button>
            </form>
        </body>
    </html>
    """

@app.post("/predict", response_class=HTMLResponse)
def predict(age: int = Form(...), salary: float = Form(...)):
    input_data = np.array([[age, salary]])
    prediction = model.predict(input_data)[0]

    result = "Will Purchase" if prediction == 1 else "Will Not Purchase"

    return f"""
    <html>
        <body style="font-family: Arial; padding: 40px;">
            <h2>Prediction Result</h2>
            <p><strong>Age:</strong> {age}</p>
            <p><strong>Salary:</strong> {salary}</p>
            <p><strong>Prediction:</strong> {result}</p>
            <br>
            <a href="/">Try Again</a>
        </body>
    </html>
    """