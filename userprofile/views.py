from django.shortcuts import render, HttpResponse


def profile_list(request):
    return render(request, 'profile_list.html')


def profile_detail(request):
    return render(request, 'profile_detail.html')


def log_in(request):
    return render(request, 'account/login.html')


def signup(request):
    return render(request, 'account/signup.html')
