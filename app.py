from flask import Flask, render_template,request
import pickle

model=pickle.load(open("model_randomforest.pkl","rb"))
app=Flask(__name__)

@app.route('/')
def loadpage():
    return render_template('about.html')

@app.route('/predict')
def predict():
    return render_template('index.html')

@app.route('/y_predict', methods=['POST'])
def prediction():
    
    Age=request.form["Age"]
    SystolicBP=request.form["SystolicBP"]
    DiastolicBP=request.form["DiastolicBP"]
    BS=request.form["BS"]
    BodyTemp=request.form["BodyTemp"]
    
    p=[[float(Age),float(SystolicBP),float(DiastolicBP),float(BS),float(BodyTemp)]]
    prediction=model.predict(p)
    
    if (prediction == ['High risk']):
        text= "Patient is at High Risk"
    elif (prediction == ['Mid risk']):
        text= "Patient is at Mid Risk"
    else:
        text="Patient is at Low Risk"
    
    return render_template("index.html",prediction_test=text)
    
    

if __name__=='__main__':
    app.run(debug=False)
