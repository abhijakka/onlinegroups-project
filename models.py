from django.forms import CharField
from django.db import models

class jobportal(models.Model):
    
        user_name=models.CharField(help_text='user_name' , max_length=50,null=True)
        user_email=models.CharField(help_text='user_email' , max_length=50,null=True)
        user_mobile_no=models.BigIntegerField(elp_text='user_mobile' , max_length=50,null=True)
        user_upload_resume=models.FileField(help_text='user_upload_resume' ,null=True)
        user_type=models.CharField(help_text='user_type' ,null=True)
        
       
        class Meta: 
                db_table='job_details' 
        
class employeeportal(models.Model):    
        employee_details=models.ForeignKey(jobportal,models.CASCADE)
        employee_post_job=models.FileField(help_text='employee_post_job' , max_length=50,null=True)
class Meta: 
        db_table='employee_details'         