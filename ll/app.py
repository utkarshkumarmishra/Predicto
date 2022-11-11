from flask import Flask, render_template, request
import pickle
import numpy as np
modellep = pickle.load(open('LEP\LR_loan.pkl', 'rb'))
modelccdr = pickle.load(open('CC\cc.pkl', 'rb'))  
app = Flask(__name__)  # initializing Flask app
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/lep")
def lep():
    return render_template('lep.html')
@app.route("/ccdr")
def ccdr():
    return render_template('ccdr.html')
@app.route("/home")
def home():
    return render_template('index.html')
@app.route("/predictlep", methods=['POST'])
def predictlep():
     if request.method == 'POST':
        d1 = request.form['Married']
        if d1 == 'No':
            d1 = 0
        else:
            d1 = 1
    
        d2 = request.form['Gender']
        if (d2 == 'Male'):
            d2 = 1
        else:
            d2 = 0
        d3 = request.form['Education']
        if (d3 == 'Graduate'):
            d3 = 1
        else:
            d3 = 0
        d4 = request.form['Self_Employed']
        if (d4 == 'No'):
            d4 = 0
        else:
            d4 = 1
        d5 = request.form['ApplicantIncome']
        d6 = request.form['CoapplicantIncome']
        d7 = request.form['LoanAmount']
        d8 = request.form['Loan_Amount_Term']
        d9 = request.form['Credit_History']
        if (d9 == 'All debts paid'):
            d9 = 1
        else:
            d9 = 0
        d10 = request.form['Property_Area']
        if (d10 == 'Urban'):
            d10 = 2
        elif (d10 == 'Rural'):
            d10 = 0
        else:
            d10 = 1
        d11 = request.form['Dependents']
        if (d11 == '3+'):
            d11 = 3
        elif (d11=='2'):
            d11 = 2
        elif (d11=='1'):
            d11 = 1
        else:
            d11 = 0
     arr = np.array([[d3, d1, d11, d3, d4, d5, d6, d7, d8,d9,d10]])
     pred = modellep.predict(arr)
     if pred == 0:
        return render_template('lep.html', prediction_text="Sorry! You are not eligible for Loan.")
     else:
        return render_template('lep.html', prediction_text="Congrats! You are eligible for Loan.")
     return render_template('lep.html')
@app.route("/predictccdr")
def predictccdr():
     if request.method == 'POST':
        d1 = request.form['Married']
        if d1 == 'No':
            d1 = 0
        else:
            d1 = 1
    
        d2 = request.form['Gender']
        if (d2 == 'Male'):
            d2 = 1
        else:
            d2 = 0
        d3 = request.form['Education']
        if (d3 == 'Graduate'):
            d3 = 1
        else:
            d3 = 0
        d4 = request.form['Self_Employed']
        if (d4 == 'No'):
            d4 = 0
        else:
            d4 = 1
        d5 = request.form['ApplicantIncome']
        d6 = request.form['CoapplicantIncome']
        d7 = request.form['LoanAmount']
        d8 = request.form['Loan_Amount_Term']
        d9 = request.form['Credit_History']
        if (d9 == 'All debts paid'):
            d9 = 1
        else:
            d9 = 0
        d10 = request.form['Property_Area']
        if (d10 == 'Urban'):
            d10 = 2
        elif (d10 == 'Rural'):
            d10 = 0
        else:
            d10 = 1
        d11 = request.form['Dependents']
        if (d11 == '3+'):
            d11 = 3
        elif (d11=='2'):
            d11 = 2
        elif (d11=='1'):
            d11 = 1
        else:
            d11 = 0
     arr = np.array([[d3, d1, d11, d3, d4, d5, d6, d7, d8,d9,d10]])
     pred = modelccdr.predict(arr)
     if pred == 0:
        return render_template('ccdr.html', prediction_text="OOPS! This customer can default.")
     else:
        return render_template('ccdr.html', prediction_text="Voilla! This customer is safe.")
     return render_template('ccdr.html')

app.run(debug=True)