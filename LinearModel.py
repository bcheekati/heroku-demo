import numpy as np
from flask import Flask, redirect, url_for, request, render_template
import pickle

app = Flask(__name__)
simpleLinearModel = pickle.load(open('simpleLinearModel.pickle', 'rb'))

@app.route('/')
def home():
   return render_template('linearmodel.html')

@app.route('/success/<x_values>')
def success(x_values):
   return 'Result Value is %s' % x_values

@app.route('/linearmodel',methods = ['POST', 'GET'])
def linearmodel():
   if request.method == 'POST':
      x_values = request.form['x_values']
      final_features = np.array([[int(x_values)]])
      prediction = round(np.float(simpleLinearModel.predict(final_features)))
      #return redirect(url_for('success',x_values = np.float(prediction)))
      return render_template('linearmodel.html', prediction = 'Employee Salary Should be {}'.format(prediction))

if __name__ == '__main__':
   app.run(debug = True)