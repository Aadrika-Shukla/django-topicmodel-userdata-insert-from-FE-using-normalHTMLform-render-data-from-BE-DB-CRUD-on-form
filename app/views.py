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

'''
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
    '''


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






''' ####### retrieving my retrieval functions after user enters some new data in respective tables 
so that the user can see whatever the data he entered is added into database or not
this will show(display) all the data after any insertion operation is done

 #####'''




def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)
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
        QLWO=WebPage.objects.all()
        d={'QLWO':QLWO}
        return render(request,'display_webpage.html',d)
        
    
        


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
        QLAO=AccessRecord.objects.all()
        d={'QLAO':QLAO}
        return render(request,'display_access.html',d)
    return render(request,'insert_access.html',d)#sending the topic objects from be to fe







'''for retrieving the data based on the data user selected if user selects multiple data then we will use 
getlist()to collect the multiple data from dropdown list
dropdown list is not preferred because it will allow you to select multiple rows but in same order
in between options you can't select for that we will go to checkbox
we will use none() here to create an emptyqueryset'''



#########     retrieving for all the tables based on filter(condition)    #######

#==============using dropdown list here for choosing multiple options=============#


###defining our functions for  multiple options dropdown retrieval###

def display_webpage_dropdown(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        STL=request.POST.getlist('tn')
        WOS=WebPage.objects.none()
        for t in STL:
            WOS=WOS|WebPage.objects.filter(topic_name=t)
        d1={'WOS':WOS}
        return render(request,'display_webpage_dropdown.html',d1)
    return render(request,'select_multiple_webpage_dropdown.html',d)

def display_access_dropdown(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        SNL=request.POST.getlist('n')
        AOS=AccessRecord.objects.none()
        for n in SNL:
            AOS=AOS|AccessRecord.objects.filter(name=n)
        d1={'AOS':AOS}
        return render(request,'display_access_dropdown.html',d1)
    return render(request,'select_multiple_access_dropdown.html',d)
        

def display_topic_dropdown(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        STL=request.POST.getlist('tn')
        TOS=Topic.objects.none()
        for t in STL:
            TOS=TOS|Topic.objects.filter(topic_name=t)
        d1={'TOS':TOS}
        return render(request,'display_topic_dropdown.html',d1)
    return render(request,'select_multiple_topics_dropdown.html',d)









#==============using dropdown list here for choosing multiple options=============#


##############      RETRIEVAL OF THE DATA BASED ON CONDITIONS   SELECTED BY THE USER  ###############




def select_multiple_topics_dropdown(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        STL=request.POST.getlist('tn')
        TOS=Topic.objects.none()
        for t in STL:
            TOS=TOS|Topic.objects.filter(topic_name=t)
        d1={'TOS':TOS}
        return render(request,'display_topic_dropdown.html',d1)

    return render(request,'select_multiple_topics_dropdown.html',d)



def select_multiple_webpage_dropdown(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        STL=request.POST.getlist('tn')
        WOS=WebPage.objects.none()
        for t in STL:
            WOS= WOS|WebPage.objects.filter(topic_name=t)
        d1={'WOS':WOS}
        return render(request,'display_webpage_dropdown.html',d1)

    return render(request,'select_multiple_webpage_dropdown.html',d)




def select_multiple_access_dropdown(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        SNL=request.POST.getlist('n')
        AOS=AccessRecord.objects.none()
        for n in SNL:
            AOS= AOS|AccessRecord.objects.filter(name=n)
        d1={'AOS':AOS}
        return render(request,'display_access_dropdown.html',d1)

    return render(request,'select_multiple_access_dropdown.html',d)





##################===============checkbox for all the tables===========######################

                    #-----------------action attribute usage----------------------#


def topic_checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    #as we are using action attribute in our topic.html and provided the url of select_multiple_topics_dropdown it will take the whole working of the select_multiple_topics_dropdown function here only the display page we will render here will be different topic_checkbox to create checkboxes for  all topic names
    return render(request,'topic_checkbox.html',d)



def webpage_checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    #as we are using action attribute in our topic.html and provided the url of select_multiple_webpage_dropdown it will take the whole working of the select_multiple_webpage_dropdown function here only the display page we will render here will be different webpage_checkbox to create checkboxes for  all topic names and then display webpages data for that selected topic name
    return render(request,'webpage_checkbox.html',d)


def access_checkbox(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    #as we are using action attribute in our topic.html and provided the url of select_multiple_access_dropdown it will take the whole working of the select_multiple_access_dropdown function here only the display page we will render here will be different access_checkbox to create checkboxes for  all  names and then display access records data for that selected  name
    return render(request,'access_checkbox.html',d)














''' ####### retrieving my retrieval functions after user enters updates some data in respective tables 
so that the user can see whatever the data he modified is added into database or not #####'''


#for updating existing topic names present in my database for topic table

def update_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        new_topic_name= request.POST['new_topic_name']
        TO=Topic.objects.filter(topic_name=tn).update(topic_name=new_topic_name)
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'update_topic.html',d)



#for updating existing WEBPAGE DATA present in my database for WEBPAGE table


def update_webpage(request):
    QLWO = WebPage.objects.all()  # TO DISPLAY ALL THE WEBPAGES NAMES IN FE
    d = {'QLWO': QLWO}  # Pass webpages to the template

    if request.method == 'POST':
        n = request.POST.get('n')  # Get selected  name
        new_name = request.POST.get('new_name')  # Get new name
        new_url = request.POST.get('new_url')  # Get new URL
        new_email = request.POST.get('new_email')  # Get new email

        # Update WebPage instances associated with the selected topic
        WO = WebPage.objects.filter(name=n).update(name=new_name,url=new_url,email=new_email)
        # Pass filtered WebPage queryset to the template
        QLWO=WebPage.objects.all()
        d = { 'QLWO': QLWO}
        return render(request, 'display_webpage.html', d)  # Redirect to a page to display updated data

    return render(request, 'update_webpage.html', d)  # Render the update form initially
   

   
#for updating existing ACCESS RECORDS DATA present in my database for ACCESS RECORDS table


def update_access(request):
    QLWO = WebPage.objects.all()  # TO DISPLAY ALL THE WEBPAGES NAMES IN FE
    d = {'QLWO': QLWO}  # Pass webpages to the template

    if request.method == 'POST':
        n = request.POST.get('n')  # Get selected  name
        new_date = request.POST.get('new_date')  # Get new date
        new_author= request.POST.get('new_author')  # Get new author

        # Update AccessRecords instances associated with the selected name
        AO = AccessRecord.objects.filter(name=n).update(date=new_date,author=new_author)
        # Pass filtered ACCESS RECORDS queryset to the template
        QLAO=AccessRecord.objects.all()
        d = {'QLAO': QLAO}
        return render(request, 'display_access.html', d)  # Redirect to a page to display updated data

    return render(request, 'update_access.html', d)  # Render the update form initially




''''    #####################    DELETION OF FORM DATA ###############################   '''


#DELETING TOPIC TABLE DATA


#to delete a specific topic name from topic table from our database



def delete_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.filter(topic_name=tn).delete()
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'delete_topic.html',d)




#to delete a specific webpage based on the  name selected by user from Webpage table from our database

def delete_webpage(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        n=request.POST['n']
        WO=WebPage.objects.filter(name=n).delete()
        QLWO=WebPage.objects.all()
        d={'QLWO':QLWO}
        return render(request,'display_webpage.html',d)
    return render(request,'delete_webpage.html',d)


#to delete a specific access record  based on the  name selected by user from Access  Record table from our database


def delete_access(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    if request.method=='POST':
        n=request.POST['n']
        AO=AccessRecord.objects.filter(id=n).delete()
        QLAO=AccessRecord.objects.all()
        d={'QLAO':QLAO}
        return render(request,'display_access.html',d)
    return render(request,'delete_access.html',d)
















