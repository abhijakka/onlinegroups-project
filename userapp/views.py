from django.shortcuts import render,redirect,HttpResponse,get_object_or_404

from userapp.models import *
from adminapp.models import *

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


# mainpage

def home(request):
    education=Groupcreatemodel.objects.order_by('-group_reg_date').filter(group_Type='Education').first()
    sports=Groupcreatemodel.objects.order_by('-group_reg_date').filter(group_Type='Sports').first()
    movies=Groupcreatemodel.objects.order_by('-group_reg_date').filter(group_Type='Movies').first()
    entertainment=Groupcreatemodel.objects.order_by('-group_reg_date').filter(group_Type='Entertainment').first()
    return render(request,'user/index.html',{'education':education,'sports':sports,'movies':movies,'entertainment':entertainment})

def about(request):
    
    return render(request,'user/about.html')

def contact(request):
    
    return render(request,'user/contact.html')
def user_about(request):
    
    return render(request,'user/user-about.html')
def user_contact(request):
    user=request.session['user_id']
    data=UserRegistrationModel.objects.filter(user_id=user)
    print(data)
    if request.method=="POST" :
       user_feeback_name=request.POST.get('name')
       user_feedback_email=request.POST.get('email')
       user_feedback_describtion=request.POST.get('message')
       user_feedback_group_name=request.POST.get('group_name')
       user=UserFeedbacks.objects.create(user_feedback_group_name=user_feedback_group_name,user_feeback_name=user_feeback_name,user_feedback_email=user_feedback_email,user_feedback_describtion=user_feedback_describtion)
       user.save()
    return render(request,'user/user-contact.html',{'data':data})

def latest_join_groups(request):
    data=Groupcreatemodel.objects.all()
    return render(request,'user/new-groups.html',{'data':data})

def news_feeds(request):
        data=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_user_view='Public').all()
        education=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Education').count()
        entertaiment=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Entertainment').count()
        sports=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Sports').count()
        movies=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Movies').count()

        if request.method=="POST" and 'btn2'in request.POST :
            
          
            search=request.POST.get('search')
        
            print(search)
            data=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(Q(upload_group_type__icontains=search))

        
            # user1=UserUploadFileModel.objects.filter(upload_group_type__icontains=search)
            # user1.save()
            
    
        return render(request,'user/news-feeds.html',{'data':data,'education':education,'entertaiment':entertaiment,'sports':sports,'movies':movies})

# userpage

def user_dashboard(request):
    user=request.session['user_id']
    data=UserUploadFileModel.objects.filter(upload_user_id=user).count()
    data3=UserUploadFileModel.objects.filter(upload_user_id=user).aggregate(payment=Sum('search_rank'))
    print(data3)
    data2=Userdownloads.objects.filter(download_user_id=user).count()
    return render(request,'user/user-dashboard.html',{'data':data,'data2':data2,'data3':data3})

def user_profile(request):
        data=request.session['user_id']
        user_profile=UserRegistrationModel.objects.filter(user_id=data).all()
        obj= get_object_or_404(UserRegistrationModel,user_id=data)

        if request.method =='POST'and request.FILES['user_upload']:

            user_name=request.POST.get('user_name')
            user_mobilenumber=request.POST.get('user_mobile')
            user_email=request.POST.get('user_email')
            user_upload_image=request.FILES['user_upload']

            obj.user_name=user_name
            obj.user_mobilenumber=user_mobilenumber
            obj.user_email=user_email
            obj.user_upload_image=user_upload_image

            obj.save(update_fields=['user_name','user_mobilenumber','user_email','user_upload_image'])
    
        return render(request,'user/my-profile.html',{'data':user_profile})

def user_latest_join_groups(request):
    user=request.session['user_id']
    data=Groupcreatemodel.objects.all()
    user_profile=UserRegistrationModel.objects.all().filter(user_id=user)
    
    # if request.method =='POST':
          
    #     group_username=request.POST.get('user_name')
    #     group_user_type=request.POST.get('user_type')
    #     group_name=request.POST.get('group_name')
    #     group_user_image=request.POST.get('user_upload_image')
    #     group_type=request.POST.get('group_Type')
    #     group_user_email=request.POST.get('user_email')
    #     group_describtion=request.POST.get('group_describtion')
    #     group_image=request.POST.get('group_upload_image')
        
    #     user=UserGroupJoin.objects.create(group_user_email=group_user_email,group_user_id=user,group_image=group_image,group_describtion=group_describtion,group_type=group_type,group_username=group_username,group_user_type=group_user_type,group_name=group_name,group_user_image=group_user_image)
    #     user.save()
    #     if user:
    #         messages.success(request,"Request sent successfully. please wait for Accept")       
    #     else:
    #         pass
        
    return render(request,'user/user-latest-groups.html',{'data':data,'data2':user_profile})

def user_join_button(request,id) :
    print(id)
    user=request.session['user_id']
    data=Groupcreatemodel.objects.get(group_id=id)
    print(data)
    user_profile=UserRegistrationModel.objects.all().filter(user_id=user)
        
    if request.method =='POST':
        print('abhi')   
        group_username=request.POST.get('user_name')
        group_user_type=request.POST.get('user_type')
        group_name=request.POST.get('group_name')
        group_user_image=request.POST.get('user_upload_image')
        group_type=request.POST.get('group_Type')
        group_user_email=request.POST.get('user_email')
        group_describtion=request.POST.get('group_describtion')
        group_image=request.POST.get('group_upload_image')
        
        user=UserGroupJoin.objects.create(group_id2=id,group_user_email=group_user_email,group_user_id=user,group_image=group_image,group_describtion=group_describtion,group_type=group_type,group_username=group_username,group_user_type=group_user_type,group_name=group_name,group_user_image=group_user_image)
        user.save()
       
        if user:
            messages.success(request,"Request sent successfully. please wait for Accept",{'data':data,'data2':user_profile})       
        else:
            pass
    return redirect('user_latest_join_groups')
def user_suggested_join(request) :
    user=request.session['user_id']
    data=Groupcreatemodel.objects.all()
    data5=UserGroupJoin.objects.all()

    
    print(data.query)
    
    user_profile=UserRegistrationModel.objects.all().filter(user_id=user)
    
    return render(request,'user/user-suggested-groups.html',{'data5':data5,'data':data,'data2':user_profile})
    

def user_suggested_join_button(request,id) :
    print(id)
    user=request.session['user_id']
    data=Groupcreatemodel.objects.get(group_id=id)
    data5=UserGroupJoin.objects.filter(group_id2=id)
    print(data5)
    print(data)
    user_profile=UserRegistrationModel.objects.filter(user_id=user)
        
    if request.method =='POST'and 'btn5'in request.POST  :
        print('abhi')   
        group_username=request.POST.get('user_name')
        group_user_type=request.POST.get('user_type')
        group_name=request.POST.get('group_name')
        group_user_image=request.POST.get('user_upload_image')
        group_type=request.POST.get('group_Type')
        group_user_email=request.POST.get('user_email')
        group_describtion=request.POST.get('group_describtion')
        group_image=request.POST.get('group_upload_image')
        
        user=UserGroupJoin.objects.create(group_id2=id,group_user_email=group_user_email,group_user_id=user,group_image=group_image,group_describtion=group_describtion,group_type=group_type,group_username=group_username,group_user_type=group_user_type,group_name=group_name,group_user_image=group_user_image)
        user.save()
       
        if user:
            messages.success(request,"Request sent successfully. please wait for Accept",{'data5':data5,'data':data,'data2':user_profile})       
        else:
            pass
        return redirect('user_suggested_join')

def user_news_feeds(request) :
    user=request.session['user_id']
    
    # education = UserUploadFileModel.objects.filter(cause = "Livelihood", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    
    data=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_user_id=user).filter(upload_user_view='Private').all()
    data2=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_user_id=user).filter(upload_user_view='Public').all()
    education=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Education').count()
    entertaiment=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Entertainment').count()
    sports=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Sports').count()
    movies=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type='Movies').count()
    if request.method=="POST" and 'btn2'in request.POST :
          
        search=request.POST.get('search')
        
        print(search)
        data=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_user_id=user).filter(Q(upload_group_type__icontains=search))

        
        user1=UserUploadFileModel.objects.filter(upload_status='Accepted').filter(upload_group_type__icontains=search).update(search_rank=F('search_rank')+1)
    
        print(user1)
       
    if request.method=="POST" and 'btn'in request.POST:
        user=request.session['user_id']
        downloads=request.POST.get('upload_id')
        user=Userdownloads.objects.create(downloads=downloads,download_user_id=user)
        user.save()
        
   
          
    return render(request,'user/user-news-feeds.html',{'data':data,'data2':data2,'education':education,'entertaiment':entertaiment,'sports':sports,'movies':movies})


def user_upload_files(request,id):
    
    user=request.session['user_id']
    user_profile=UserRegistrationModel.objects.all().filter(user_id=user)
    group=UserGroupJoin.objects.filter(group_id=id)

    if request.method =='POST' and request.FILES['fileToUpload']:
          
        upload_group_name=request.POST.get('groupname')
        upload_user_view=request.POST.get('user_view')
        upload_post_name=request.POST.get('user_post_name')
        upload_describtion=request.POST.get('user_describtion')
        upload_File=request.FILES['fileToUpload']
        upload_user_name=request.POST.get('user_name')
        upload_group_type=request.POST.get('group_type')
        upload_user_email=request.POST.get('user_email')
        upload_user_location=request.POST.get('user_location')
        user=UserUploadFileModel.objects.create(upload_user_location=upload_user_location,upload_user_email=upload_user_email,upload_group_type=upload_group_type,upload_user_name=upload_user_name,upload_user_id=user,upload_group_name=upload_group_name,upload_user_view=upload_user_view,upload_post_name=upload_post_name,upload_describtion=upload_describtion,upload_File=upload_File)
        user.save()
    return render(request,'user/user-upload-files.html',{'data':user_profile,'data2':group})

def user_view_accepted_groups(request):
    user= data=request.session['user_id']
    data=UserGroupJoin.objects.filter(group_user_id=user)
    
    return render(request,'user/user-view-groups.html',{'data':data})


def user_registration(request):
    
    if request.method =='POST' and request.FILES['user_upload']:
      
        user_name=request.POST.get('user_name')
        user_mobilenumber=request.POST.get('user_mobile')
        user_email=request.POST.get('user_email')
        user_password=request.POST.get('user_password')
        user_location=request.POST.get('location')
        user_type=request.POST.get('user_type')
        user_interest=request.POST.get('sports')
        
        user_upload_image=request.FILES['user_upload']
        user=UserRegistrationModel.objects.create(user_name=user_name,user_mobilenumber=user_mobilenumber,user_email=user_email,user_password=user_password,user_location=user_location,user_type=user_type,user_interest=user_interest,user_upload_image=user_upload_image)
        user.save()
        
        if user:
            messages.success(request,"Your Registration Form Is Successfully Uploaded")       
        else:
            pass
    return render(request,'user/register.html')

def user_login(request):
      if request.method == 'POST': 
                email = request.POST.get('user_email') 
                password = request.POST.get('user_password') 
                try: 
                     check = UserRegistrationModel.objects.get(user_email=email,user_password=password)   
                     request.session['user_id']=check.user_id  
                       
                     user_status = check.user_status 
                     if user_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('user_dashboard')  
                     elif user_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif user_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
 
                      
                except: 
                     messages.warning(request,'invalid login') 
    
      return render(request,'user/login.html')    
    
       
   