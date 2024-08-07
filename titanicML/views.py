from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def result(request):
    user_input_age = request.GET['age']
    user_input_age += ' take the chance'
    return render(request, 'results.html', {'age': user_input_age})
