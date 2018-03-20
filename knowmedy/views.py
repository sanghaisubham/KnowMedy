import time
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from .forms import MainForm,Sympform
from django.views.decorators.http import require_POST
from .HINT_Scraper import disease
from .models import MainModel
from .HINT_Scraper import Disease_Predicting
import json

# Create your views here.
def index(request):
    form = MainForm()
    return render(request,'knowmedy/index.html',{'form':form})

def findtub(request):
    return render(request,'knowmedy/findtub.html')

def login(request):
    return render(request,'knowmedy/login.html')

def search(request):
    symform = Sympform()
    return render(request,'knowmedy/search.html',{'form':symform})

@require_POST
def find(request):
    form = MainForm(request.POST)
    model = MainModel.objects.extra(select={'diff': 'upvote-downvote'}).order_by('-diff')
    if form.is_valid():
        name = form.cleaned_data['name']
        flag=1
        if MainModel.objects.filter(name=name).exists():
            mo = MainModel.objects.get(name=name)
            symptoms = mo.symptoms
            causes = mo.causes
            complications = mo.complications
            introduction = mo.introduction
            diagnosis = mo.diagnosis

            #return HttpResponse('It is already there in the database!')
        else:
            symptoms = disease.symptoms(name)
            causes = disease.causes(name)
            complications = disease.complications(name)
            diagnosis = disease.diagnosis(name)
            introduction = disease.introduction(name)
            new_model = MainModel(name=name, symptoms=symptoms, causes = causes, diagnosis=diagnosis,complications=complications, introduction=introduction)
            new_model.save()
            #dava = disease.medicine_finder(name)
        context = {'name':name,'symptoms':symptoms,'causes':causes,'complications':complications,'model':model,'diagnosis':diagnosis,'introduction':introduction}
        return render(request,'knowmedy/find.html',context)

def get_disease(request):
    symform = Sympform(request.POST)
    result = {}
    s = ''
    if symform.is_valid():
        attribute_set = {}
        attribute_set[symform.cleaned_data['symptoms1']] = symform.cleaned_data['severity1']
        attribute_set[symform.cleaned_data['symptoms2']] = symform.cleaned_data['severity2']
        attribute_set[symform.cleaned_data['symptoms3']] = symform.cleaned_data['severity3']
        # for k, v in attribute_set.items():
        #    s+=k+' : '+str(v)+' , '
        # return HttpResponse(s)
        reli=[]
        result = Disease_Predicting.disease(attribute_set)
        for i,dictit in result.items():
            for k,v in dictit.items():
                reli.append({k:v})
        #result = json.dumps(result)
        return render(request,'knowmedy/showresults.html',{'reli':reli})


def likes_increase(request,todo_id):
    todo = MainModel.objects.get(pk=todo_id)
    todo.upvote+=1
    todo.save()
    return redirect('find')

def dislikes_increase(request,todo_id):
    todo = MainModel.objects.get(pk=todo_id)
    todo.downvote+=1
    todo.save()
    return redirect('find')


