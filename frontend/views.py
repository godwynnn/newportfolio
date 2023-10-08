from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect,render,get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .emailsender import sendmail
from django.conf import settings
# Create your views here.

class IndexView(View):
    
    myemail='miraclegodwin67@gmail.com'
    def get(self,request,*args,**kwargs):
        context={}


        context['title']='Home'
        context['year']=datetime.datetime.now().year
        context['diff']=datetime.datetime.now().year-2019
        return render(request,'frontend/index.html',context)

    def post(self,request,*args,**kwargs):
        username=request.POST.get('username')
        user_email=str(request.POST.get('email')).strip()
        message=request.POST.get('message')

        # send_mail(
        #     'message from '+ str(username),
        #     message,
        #     user_email,
        #     [self.myemail],
        #     fail_silently=False

        # )
        sendmail([settings.EMAIL_HOST_USER],message,message,email=user_email)


        # email.send()
        return HttpResponseRedirect(reverse('index'))