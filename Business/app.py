from flask import *

import numpy as np
import pickle


app = Flask(__name__, template_folder= 'templates')

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello():
    return render_template("ann.html")

@app.route('/predict', methods = ['post', 'get'])
def predict():
    int_features = []
    for x in request.form.values():
        if x == 'France':
            int_features.append(1)
            int_features.append(0)
            int_features.append(0)

        elif x == 'Spain':
            int_features.append(0)
            int_features.append(0)
            int_features.append(1)
  
        elif x == 'Germany':
            int_features.append(0)
            int_features.append(1)
            int_features.append(0)

        elif x == 'Male' :
            int_features.append(1)

        elif x == 'Female':
            int_features.append(0)

        elif x == 'Yes':
            int_features.append(1)

        elif x == 'No':
            int_features.append(0)

        else:
            int_features.append(int(x))

    final = [int_features]
    print(int_features)
    print(final)
    prediction = model.predict(final)

    if prediction > [[0.5]]:
        print("He will Stay")
        return render_template('ann.html')
    else:
        print("He will not Stay")
        return render_template('ann.html')


if __name__ == '__main__':
    app.run(debug = True)