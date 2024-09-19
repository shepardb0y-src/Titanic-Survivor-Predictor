from django.shortcuts import render
from . import fake_model


def home(request):
    return render(request, 'index.html')


def result(request):
    user_input_age = request.GET['age']
    prediction = fake_model.fake_predict(user_input_age)
    return render(request, 'results.html', {'prediction': prediction})
