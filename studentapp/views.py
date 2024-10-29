from django.shortcuts import render,redirect

def StudentHomePage(request):
    return render(request, 'studentapp/StudentHomePage.html')