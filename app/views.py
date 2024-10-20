from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.
def hii(request):
    import calendar
    d=calendar.month(2001,9)
    s=f"<h1>{str(d)} </h1>"
    return HttpResponse(s)

