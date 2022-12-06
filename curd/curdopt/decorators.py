from django.http import HttpResponse 
from django.shortcuts import render ,redirect
def unauthentocated_user(view):
    def wrapper_func(request ,*args ,**kwargs):
        if request.user.is_authenticated():
            return redirect('intro')
        else:
            return view(request ,*args ,**kwargs)
    return wrapper_func