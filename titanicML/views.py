from django.shortcuts import render
from . import ml_predict


def home(request):
    return render(request, 'index.html')


def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])
    prediction = ml_predict.prediction_model()
    return render(request, 'results.html', {'prediction': prediction})
