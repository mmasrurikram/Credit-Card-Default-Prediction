import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('pickle.pkl', 'rb'))
    
@app.route('/')
def home():
    return render_template('index.html')
   

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        LIMIT_BAL=int(request.form["LIMIT_BAL"])
        PAY_0=int(request.form["PAY_0"])
        PAY_2=int(request.form["PAY_2"])
        PAY_3=int(request.form["PAY_3"])
        PAY_4=int(request.form["PAY_4"])
        PAY_5=int(request.form["PAY_5"])
        PAY_6=int(request.form["PAY_6"])
        PAY_AMT1=int(request.form["PAY_AMT1"])
        PAY_AMT2=int(request.form["PAY_AMT2"])
        PAY_AMT3=int(request.form["PAY_AMT3"])
        PAY_AMT6=int(request.form["PAY_AMT6"])
        
        
                      
        data = np.array([[LIMIT_BAL,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT6]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
              
if __name__ == '__main__':
    app.run(host="localhost", port=2000)