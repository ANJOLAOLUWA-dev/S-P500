@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        try:
            open_val = float(request.form["open"])
            high_val = float(request.form["high"])
            low_val = float(request.form["low"])
            close_val = float(request.form["close"])

            input_df = pd.DataFrame([[open_val, high_val, low_val, close_val]], columns=["Open", "High", "Low", "Close"])
            prediction = round(best_model.predict(input_df)[0], 2)
        except:
            prediction = "Invalid input"

    return render_template_string(form_template, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
