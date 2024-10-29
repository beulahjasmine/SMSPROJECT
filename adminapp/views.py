from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render,redirect,get_object_or_404
def projecthomepage(request):
    return render(request,'adminapp/ProjectHomePage.html')

def printpagecall(request):
    return render(request,'adminapp/Printer.html')
def printpagelogic(request):
    if request.method=="POST":
        User_input=request.POST['User_input']
        print(f'User input: {User_input}')
    a1= {'User_input':User_input}
    return render(request, 'adminapp/Printer.html',a1)

def exceptionpagelogic(request):
    if request.method=="POST":
        User_input=request.POST['User_input']
        result=None
        error_message=None
        try:
            num=int(User_input)
            result=10/num
        except Exception as e:
            error_message=str(e)
        return render(request,'adminapp/ExceptionExample.html',{'result':result,'error':error_message})
    return render(request,'adminapp/ExceptionExample.html')

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

from django.contrib.auth.models import User, auth
from django.shortcuts import render

def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['Username']
        first_name = request.POST['First_Name']
        last_name = request.POST['Last_Name']
        email = request.POST['Email_ID']
        pass1 = request.POST['Password']
        pass2 = request.POST['Confirm_Password1']

        if pass1 == pass2:
            if User.objects.filter(Username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(Email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    Username=username,
                    Password=pass1,
                    First_Name=first_name,
                    Last_Name=last_name,
                    Email_ID=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')

def UserRegisterpagecall(request):
    return render(request, 'adminapp/Register.html')



from .forms import *
def add_task(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
    tasks=Task.objects.all()
    return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks} )

def delete_task(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')
from django.contrib import messages
from django.contrib.auth import authenticate, login

def UserLoginPageCall(request):
    return render(request, 'adminapp/Login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/Login.html')
    else:
        return render(request, 'adminapp/Login.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

from . forms import StudentForm
from . models import StudentList


def add_student(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form':form})
def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html',{'students': students})
def datetimepagecall(request):
    return render(request,'adminapp/datetimepage.html')

import datetime
import calendar
from datetime import timedelta

from datetime import datetime, timedelta
import calendar
from django.shortcuts import render


def datetimepagelogic(request):
    if request.method == "POST":
        number1 = int(request.POST['date1'])
        x = datetime.now()
        ran = x + timedelta(days=number1)
        ran1 = ran.year
        ran2 = calendar.isleap(ran1)
        if ran2 == False:
            ran3 = "Not a Leap Year"
        else:
            ran3 = "Leap Year"
        a1 = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
    else:
        a1 = {'ran': None, 'ran3': None, 'ran1': None, 'number1': None}

    return render(request, 'adminapp/datetimepage.html', a1)


import random
import string

def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')

def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran':ran}
    return render(request,'adminapp/randomexample.html',a1)


def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})







