from django.shortcuts import render

def signin(request):
    context = {
         
    }
    return render(request, 'users/signin.html', context)

def signup(request):
    context = {
         
    }
    return render(request, 'users/signup.html', context)