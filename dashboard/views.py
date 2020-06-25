from django.shortcuts import render

def home(request):
    context = {
         
    }
    return render(request, 'dashboard/index.html', context)

def signout(request):
    context = {
         
    }
    return render(request, 'users/logout.html', context)

def profile(request):
    context = {
         
    }
    return render(request, 'dashboard/profile_user.html', context)
