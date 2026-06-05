from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("best_model.pkl")
model_columns = joblib.load("model_columns.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_df = pd.DataFrame([data])
        input_df = pd.get_dummies(input_df)

        for col in model_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[model_columns]

        prediction = model.predict(input_df)[0]

        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)