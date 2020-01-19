from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.

def help(request):
    my_dict={'insert_me':"Now I am coming from first_app/help.html!"}
    return render(request,'first_app/help.html',context=my_dict)


def access(request):
    access_list = AccessRecord.objects.order_by('date')
    access_dict = {"access_records":access_list}
    return render(request,'first_app/access.html',context=access_dict)

def webpage(request):
    webpages_list = Webpage.objects.all()
    webpages_dict = {"webpages_records":webpages_list}
    return render(request,'first_app/webpage.html',context=webpages_dict)

def topic(request):
    topic_list = Topic.objects.all()
    topic_dict = {"topic_records":topic_list}
    return render(request,'first_app/topic.html',context=topic_dict)
