from django.shortcuts import render
from . import ml_predict


def home(request):
    return render(request, 'index.html')


def result(request):
    age = int(request.GET['age'])
    prediction = ml_predict.prediction_nodel()
    return render(request, 'results.html', {'prediction': prediction})
