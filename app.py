#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/logistic_model.pkl', 'rb') as f:
    logistic = pickle.load(f)

with open('Models/RF_model.pkl', 'rb') as f:
    randomforest = pickle.load(f)

with open('Models/svm_clf_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)


def get_predictions(age, sex, chest_pain_type, resting_blood_pressure,cholestoral,fasting_blood_sugar,resting_electrocardiographic_results, maximum_heart_rate,
                                exercise_induced_angina, ST_depression, exercise_ST_segment, vessels_colored, thal, req_model):
    mylist = [age, sex, chest_pain_type, resting_blood_pressure,cholestoral,fasting_blood_sugar,resting_electrocardiographic_results, maximum_heart_rate,
                                exercise_induced_angina, ST_depression, exercise_ST_segment, vessels_colored, thal]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'Logistic':
        #print(req_model)
        return logistic.predict(vals)[0]

    elif req_model == 'RandomForest':
        #print(req_model)
        return randomforest.predict(vals)[0]

    elif req_model == 'SVM':
        #print(req_model)
        return svm_model.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        chest_pain_type = request.form['chest_pain_type']
        resting_blood_pressure = request.form['resting_blood_pressure']
        cholestoral = request.form['cholestoral']
        fasting_blood_sugar = request.form['fasting_blood_sugar']
        resting_electrocardiographic_results = request.form['resting_electrocardiographic_results']
        maximum_heart_rate = request.form['maximum_heart_rate']
        exercise_induced_angina = request.form['exercise_induced_angina']
        ST_depression = request.form['ST_depression']
        exercise_ST_segment = request.form['exercise_ST_segment']
        vessels_colored = request.form['vessels_colored']
        thal = request.form['thal']
        
        req_model = request.form['req_model']

        target = get_predictions(age, sex, chest_pain_type, resting_blood_pressure,cholestoral,fasting_blood_sugar,resting_electrocardiographic_results,
                                 maximum_heart_rate,exercise_induced_angina, ST_depression, exercise_ST_segment, vessels_colored, thal, req_model)

        if target==1:
            sale_making = 'patient has a diease'
        else:
            sale_making = 'patient does not have a diease'

        return render_template('home.html', target = target, sale_making = sale_making)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
