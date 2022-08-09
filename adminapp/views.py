
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from adminapp.models import *
from userapp.models import *

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.db.models import Count

from django.http import HttpResponseRedirect
from onlinegroup.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q,F

import random
# Create your views here.




def admindashboard(request):
    
    data5=UserRegistrationModel.objects.all()
    
    data1=UserRegistrationModel.objects.filter(user_status='Pending').all().count()
    data2=UserUploadFileModel.objects.all().count()
    data3=Groupcreatemodel.objects.all().count()
    if request.method=="POST" :
        print('postmethod')    
          
        search=request.POST.get('search')
    
        print(search)
        data5=UserRegistrationModel.objects.filter(Q(user_name__contains=search)|Q(user_interest__contains=search))
       
    return render(request,'admin/admin-dashboard.html',{'register':data1,'upload':data2,'groups':data3,'user':data5})


def admin_group_create(request):
     if request.method =='POST' and request.FILES['group_upload']:
          
        group_name=request.POST.get('group_name')
        group_location=request.POST.get('Group_location')
        group_Type=request.POST.get('Group_Type')
        group_describtion=request.POST.get('group_describtion')
        
        
        group_upload_image=request.FILES['group_upload']
        user=Groupcreatemodel.objects.create(group_name=group_name,group_location=group_location,group_Type=group_Type,group_describtion=group_describtion,group_upload_image=group_upload_image)
        user.save()
        
        if user:
            messages.success(request,"Your Group Form Is Successfully Uploaded")       
        else:
            pass
    
     return render(request,'admin/admin-group-create.html')
def admin_view_user_feedbacks(request):
    data=UserFeedbacks.objects.all()
     
    if request.method=="POST" :
        print('postmethod')    
          
        search=request.POST.get('search')
    
        print(search)
        data=UserFeedbacks.objects.filter(Q(user_feeback_name__contains=search)|Q(user_feedback_email__contains=search)|Q(user_feedback_group_name__contains=search))
       
    return render(request,'admin/admin-view-user-feedback.html',{'data':data})
 

def admin_view_group_details(request):
    data=Groupcreatemodel.objects.all()
    
    if request.method=="POST" :
        
        print('postmethod')    
          
        search=request.POST.get('search')
    
        print(search)
        data=Groupcreatemodel.objects.filter(Q(group_name__contains=search)|Q(group_Type__contains=search)|Q(group_location__contains=search))

    return render(request,'admin/admin-group-details.html',{'data':data})


def admin_user_register_request(request):
    data=UserRegistrationModel.objects.all()
       
    
    if request.method=="POST" :
        
        print('postmethod')    
          
        search=request.POST.get('search')
    
        print(search)
        data=UserRegistrationModel.objects.filter(Q(user_name__contains=search)|Q(user_email__contains=search)|Q(user_mobilenumber__contains=search)|Q(user_interest__contains=search)|Q(user_type__contains=search))


    return render(request,'admin/admin-user-signup-request.html',{'data':data})


def admin_user_group_join_request(request):
    data=UserGroupJoin.objects.all()
        
    
    if request.method=="POST" :
        
        print('postmethod')    
          
        search=request.POST.get('search')
    
        print(search)
        data=UserGroupJoin.objects.filter(Q(group_username__contains=search)|Q(group_name__contains=search)|Q(group_user_type__contains=search))

    
    return render(request,'admin/admin-user-group-join-request.html',{'data':data})


def admin_user_upload_file_request(request):
    data=UserUploadFileModel.objects.all()
        
    if request.method=="POST" :
        
        print('postmethod')    
          
        search=request.POST.get('search')
    
        print(search)
        data=UserUploadFileModel.objects.filter(Q(upload_group_name__contains=search)|Q(upload_post_name__contains=search)|Q(upload_user_view__contains=search))

    
    return render(request,'admin/admin-upload-request.html',{'data':data})


def admin_user_group_join_request_accept(request,id):
    
    accept = get_object_or_404(UserGroupJoin,group_id=id)
    accept.group_status = 'Accepted'
    accept.save(update_fields=['group_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> OnlineGroups Your Join Requset has been Accepted.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.group_user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("OnlineGroups Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
          if msg.send():
            return redirect('admin_user_group_join_request')
    except:
           print(msg)
             
    return redirect('admin_user_group_join_request')

def admin_user_group_join_request_Rejected(request,id):
    
    user_upload_Rejected = get_object_or_404(UserGroupJoin,group_id=id)
    user_upload_Rejected.group_status = 'Rejected'
    user_upload_Rejected.save(update_fields=['group_status'])
    user_upload_Rejected.save()
    
    #email message
    html_content = "<br/> <p> OnlineGroups Your join Request is Rejected Please Rejoin It.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [user_upload_Rejected.group_user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("OnlineGroups Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
          if msg.send():
            return redirect('admin_user_group_join_request')
    except:
           print(msg)
             
    return redirect('admin_user_group_join_request')

def user_upload_accept(request,id):
    
    accept = get_object_or_404(UserUploadFileModel,upload_id=id)
    accept.upload_status = 'Accepted'
    accept.admin_user_id = id
    accept.save(update_fields=['admin_user_id','upload_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> OnlineGroups Your Post has been Accepted.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.upload_user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("OnlineGroups Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
          if msg.send():
            return redirect('admin_user_upload_file_request')
    except:
           print(msg)
             
    return redirect('admin_user_upload_file_request')

def user_upload_Rejected(request,id):

               
        user_upload_Rejected = get_object_or_404(UserUploadFileModel,upload_id=id)
        user_upload_Rejected.upload_status = 'Rejected'
        user_upload_Rejected.admin_user_id = id
        user_upload_Rejected.save(update_fields=['upload_status','time'])
        user_upload_Rejected.save()
        #email message
        html_content = "<br/> <p> OnlineGroups Your Post is Rejected.Please ReUpload It.</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [user_upload_Rejected.upload_user_email]
        
        # if send_mail (subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("OnlineGroups Application Status",html_content,from_mail,to_mail)
        msg.attach_alternative(html_content,"text/html")
        try:
          if msg.send():
            return redirect('admin_user_upload_file_request')
        except:
           print(msg)
             
        return redirect('admin_user_upload_file_request')
        
                
    
         

def admin_user_register_request_accept(request,id):
    
    accept = get_object_or_404(UserRegistrationModel,user_id=id)
    accept.user_status = 'Accepted'
    accept.save(update_fields=['user_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> OnlineGroups Registration has been Accepted.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("OnlineGroups Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            return redirect('admin_user_register_request')
    except:
        print(msg)
             
        return redirect('admin_user_register_request')
   

def admin_user_register_request_Rejected(request,id):
    
    user_upload_Rejected = get_object_or_404(UserRegistrationModel,user_id=id)
    user_upload_Rejected.user_status = 'Rejected'
    user_upload_Rejected.save(update_fields=['user_status'])
    user_upload_Rejected.save()
    
    #email message
    html_content = "<br/> <p> OnlineGroup Registration is Rejected.Please Reapply it.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [user_upload_Rejected.user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("OnlineGroups Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            return redirect('admin_user_register_request')
    except:
        print(msg)
             
        return redirect('admin_user_register_request')


def admin_login(request):
    if request.method=='POST':
        name=request.POST.get('username') 
        password=request.POST.get('password') 
        if name=='admin@gmail.com' and password=='admin':
           return redirect('admindashboard')
    
    return render(request,'user/admin-login.html')


