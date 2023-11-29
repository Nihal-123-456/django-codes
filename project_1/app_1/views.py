from django.shortcuts import render
import datetime

# Create your views here.
def home(req):
    info = {'name':'shafin','age':10,'lst':['I','am','the','ghost'],'date':datetime.datetime.now(),
            'course':[{'id':1,'name':'phitron'},{'id':2,'name':'CSS'}],'value':"Coming here"}
    return render(req, 'index.html', info)