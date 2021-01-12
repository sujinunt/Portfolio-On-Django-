from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .contactform import TestForm
from portfolio.models import contact
from django.utils import timezone

# Create your views here.
def index(request):
    headerstr = 'Hello Boy from kratos is var1 in index'
    #template = loader.get_template('index.html')
    context = {
        'var1' : headerstr,
        'form': TestForm
    }
    if request.method == 'POST':
        print(request.POST)
        postdata = request.POST.dict()
        Email = postdata.get('Email')
        Subject = postdata.get('Subject')
        Message = postdata.get('Message')
        Message_date = timezone.now()
        emailpost = contact(email=Email,subject=Subject,message=Message,message_date=Message_date)
        emailpost.save()
        return HttpResponseRedirect('/index')
    
    return render(request,'index.html',context)
    #return HttpResponse(template.render(context,request))
