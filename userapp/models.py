from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import math

# Create your models here.
class UserRegistrationModel(models.Model):
    
    user_id=models.AutoField(primary_key=True)
    user_name=models.TextField(help_text='Enter Your username' , max_length=50)
    user_location=models.TextField(help_text='Enter Your user_location' , max_length=50)
    user_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber',max_length=50)
    user_email=models.EmailField(help_text='Enter email', max_length=50)
    user_password=models.CharField(help_text='user_password',max_length=200,null=True)
    user_interest=models.CharField(help_text='user_interest',max_length=200,null=True)
    user_type=models.CharField(help_text='user_type',max_length=200,null=True)
    user_reg_date=models.DateField(auto_now_add=True,null=True)
    user_status=models.CharField(help_text='user_status' ,default='Pending',max_length=200)
    user_upload_image=models.ImageField(help_text='user_upload_image ' , max_length=50,null=True)

    class Meta:
        db_table='user_registration_details' 


class UserUploadFileModel(models.Model):
    
    upload_id=models.AutoField(primary_key=True)
    upload_post_name=models.TextField(help_text='Enter Your upload_post_name' , max_length=50)
    upload_describtion=models.TextField(help_text='Enter Your upload_describtion' , max_length=50)
    upload_user_view=models.CharField(help_text='Enter Your upload_view',max_length=50,null=True)
    upload_group_name=models.CharField(help_text='upload_group_name',max_length=200,null=True)
    upload_date=models.DateField(auto_now_add=True,null=True)
    upload_date_time=models.DateTimeField(auto_now_add=True,null=True)
    upload_user_email=models.EmailField(help_text='upload_user_email',max_length=200,null=True)
    upload_user_location=models.CharField(help_text='upload_group_name',max_length=200,null=True)
    upload_status=models.CharField(help_text='upload_status' ,default='Pending',max_length=200)
    upload_File=models.ImageField(help_text='upload_File ' , max_length=50,null=True)
    upload_user_id=models.CharField(help_text='upload_user_id' ,max_length=200,null=True)
    upload_user_name=models.CharField(help_text='upload_user_name' ,max_length=200,null=True)
    upload_group_type=models.CharField(help_text='upload_user_name' ,max_length=200,null=True)
    admin_user_id=models.CharField(help_text='admin_user_id' ,max_length=200,null=True)
    search_rank=models.BigIntegerField(help_text='upload_user_name' ,max_length=200,default=0)
    
    
    def __str__(self):
        return self.upload_id


    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.upload_date_time

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


    class Meta:
        db_table='user_upload_file_details' 
        
class UserGroupJoin(models.Model):
    
    group_id=models.AutoField(primary_key=True)
    group_username=models.TextField(help_text='Enter Your upload_post_name' , max_length=50)
    group_user_type=models.TextField(help_text='Enter Your upload_describtion' , max_length=50)
    group_name=models.CharField(help_text='Enter Your upload_view',max_length=50)
    group_user_join_date=models.DateField(auto_now_add=True,null=True)
    group_status=models.CharField(help_text='upload_status' ,default='Pending',max_length=200)
    group_user_image=models.ImageField(help_text='upload_File ' , max_length=50,null=True)
    group_describtion=models.TextField(help_text='Enter Your upload_describtion' , max_length=50,null=True)
    group_type=models.CharField(help_text='group_type',max_length=200)
    group_user_email=models.EmailField(help_text='group_type',max_length=200,null=True)
    group_image=models.ImageField(help_text='upload_File ' , max_length=50,null=True)
    group_user_id=models.CharField(help_text='group_type',max_length=200,null=True)
    group_id2=models.CharField(help_text='group_id',max_length=200,null=True)
    class Meta:
        db_table='user_join_groups_details' 
        
class Userdownloads(models.Model):
    download_id=models.AutoField(primary_key=True)
    download_user_id=models.CharField(help_text='download_user_id' , max_length=50,null=True)
    downloads=models.CharField(help_text='downloads' , max_length=50,null=True)
    class Meta:
        db_table='user_download_details'     
        
class UserFeedbacks(models.Model):
    user_feedback_id=models.AutoField(primary_key=True)
    user_feeback_name=models.CharField(help_text='user_feeback_name' , max_length=50,null=True)
    user_feedback_email=models.EmailField(help_text='user_feedback_email' , max_length=50,null=True)
    user_feedback_group_name=models.CharField(help_text='user_feeback_group_name' , max_length=50,null=True)
    user_feedback_describtion=models.TextField(help_text='user_feedback_describtion' ,null=True)
    class Meta:
        db_table='user_feeback_details' 
        
                           