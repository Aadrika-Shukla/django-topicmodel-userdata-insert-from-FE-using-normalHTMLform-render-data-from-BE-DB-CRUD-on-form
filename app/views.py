from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *



def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic is successfully inserted to my database')
    return render(request,'insert_topic.html')





def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        RTO=Topic.objects.get(topic_name=tn)
        WO=WebPage.objects.get_or_create(topic_name=RTO,name=na,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('webpage for respective topic is successfully inserted to my database')
    
        


    return render(request,'insert_webpage.html')






def insert_access(request):
    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        at=request.POST['at']
        RWO=WebPage.objects.get(name=na)
        AO=AccessRecord.objects.get_or_create(name=RWO,date=da,author=at)[0]
        AO.save()
        return HttpResponse('record for respective topic is successfully inserted to my database')

    return render(request,'insert_access.html')