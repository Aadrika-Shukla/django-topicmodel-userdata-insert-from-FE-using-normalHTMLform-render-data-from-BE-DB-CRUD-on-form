from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


'''
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

    return render(request,'insert_access.html')'''




###### inorder to display topic names in form of dropdown list so that  user can't enter new topics as previously we are using get method so if topic is not their if will throw error and using get_or_create to create that is it is not their now user can't enter new topic for child table as we created dropdow thus eradicating that errror  ####


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic is successfully inserted to my database')
    return render(request,'insert_topic.html')





def insert_webpage(request):
    QLTO=Topic.objects.all() # to get all the objects from the topic table so that it can be sended from be to fe in order to get display it
    d={'QLTO':QLTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        RTO=Topic.objects.get(topic_name=tn)#as we sended topic_name from  fe so we are using topic_name here for comparison
        WO=WebPage.objects.get_or_create(topic_name=RTO,name=na,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('webpage for respective topic is successfully inserted to my database')
    
        


    return render(request,'insert_webpage.html',d)#sending the topic objects from be to fe






def insert_access(request):
    QLWO=WebPage.objects.all() # to get all the objects from the webpage table so that it can be sended from be to fe in order to get display it
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        at=request.POST['at']
        RWO=WebPage.objects.get(id=na)#as we sended id because it is primary key column from  fe so we are using id here for comparison
        AO=AccessRecord.objects.get_or_create(name=RWO,date=da,author=at)[0]
        AO.save()
        return HttpResponse('record for respective topic is successfully inserted to my database')

    return render(request,'insert_access.html',d)#sending the topic objects from be to fe


####   separete RETRIEVAL FUNCTIONs() created here THAT WILL GET CALLED WHEN DATA IS INSERTED,UPDATED,DELETED ######


def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)


def display_access(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)