from _curses import flash

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Calculator


def index(request):
    return render(request, 'app.html')


# def first_num(request):
#     if request.method == 'GET':
#         print('go get')
#     elif request.method == 'POST':
#         num1 = float(input('number1'))
#         print('go post')
#     return render(request, 'app.html', num1=num1)


def number_operand(request):
    if request.method == 'POST':
        name = request.form['name']
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        # if not num1 or not num2:
        #     error_message = 'All Form Fields Required..'
        #     flash('All Form Fields Required..')
        #     return render('page_not_found.html', error_message=error_message)
        # elif num2 == 0:
        #     error_zero = 'Division by 0 not allowed !!'
        #     return render('zero.html', error_zero=error_zero)

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render('index.html', sum=sum)


    elif operation == 'subtract':
        sum = float(num1) - float(num2)
        return render('index.html', sum=sum, num1=num1, num2=num2, operation=operation, name=name)


    elif operation == 'multiply':
        sum = float(num1) * float(num2)
        return render('index.html', sum=sum, num1=num1, num2=num2, operation=operation, name=name)


    elif operation == 'divide':
        try:
            sum = float(num1) / float(num2)
        except ZeroDivisionError:
            zero_message = 'Division by 0 not allowed !!'
            flash('Division by 0 not allowed !!')
            return render('zero.html', zero_message=zero_message)
    return render('index.html', sum=sum, num1=num1, num2=num2, operation=operation, name=name)
