"""
URL configuration for forms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_access/',insert_access,name='insert_access'),
    path('display_topic/',display_topic,name='display_topic'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('display_access/',display_access,name='display_access'),
    path('select_multiple_topics_dropdown/',select_multiple_topics_dropdown,name='select_multiple_topics_dropdown'),#for multiple selection using  dropdown list for topic table
    path('select_multiple_webpage_dropdown/',select_multiple_webpage_dropdown,name='select_multiple_webpage_dropdown'), # for multiple seelection from dropdown list for webpage table
    path('select_multiple_access_dropdown/',select_multiple_access_dropdown,name='select_multiple_access_dropdown'),# for multiple selection  using dropdown list for access records
    path('display_topic_dropdown/',display_topic_dropdown,name='display_topic_dropdown'),# for displaying multiple records from topic table using dropdown list
    path('display_webpage_dropdown/',display_webpage_dropdown,name='display_webpage_dropdown'),# for displaying multiple records from webpage table using dropdown list
    path('display_access_dropdown/',display_access_dropdown,name='display_access_dropdown'),# for displaying multiple records from access records table using dropdown list
    path('topic_checkbox/',topic_checkbox,name='topic_checkbox'),#for choosing multiple options using checkbox for topic table
    path('webpage_checkbox/',webpage_checkbox,name='webpage_checkbox'),#for choosing multiple options using checkbox for webpage table 
    path('access_checkbox/',access_checkbox,name='access_checkbox'),#for choosing multiple options using checkbox for access record table
    path('update_topic/',update_topic,name='update_topic'),
    path('update_webpage/',update_webpage,name='update_webpage'),
    path('update_access/',update_access,name='update_access'),



]
