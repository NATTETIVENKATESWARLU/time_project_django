from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.
def hii(request):
    import datetime
    d=datetime.datetime.now()
    s=f"<h1>hello world  {str(d)} </h1>"
    return HttpResponse(s)

