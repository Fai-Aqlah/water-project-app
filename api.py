from fastapi import FastAPI
import joblib

app = FastAPI()

# Load the trained model
model = joblib.load("xgboost_model.pkl")

@app.get("/")
def home():
    return {"message": "Smart Water Prediction API is running"}

@app.get("/predict")
def predict(previous_consumption: float, current_consumption: float):

    # حساب الفرق كما درّبتِ عليه النموذج
    consumption_diff = current_consumption - previous_consumption

    # تجهيز البيانات للموديل
    input_data = [[
        previous_consumption,
        current_consumption,
        consumption_diff
    ]]

    # عمل التنبؤ
    prediction = model.predict(input_data)[0]

    return {
        "previous": previous_consumption,
        "current": current_consumption,
        "difference": consumption_diff,
        "leak_detected": int(prediction)
    }
