from django.db import models

# Create your models here.
class Groupcreatemodel(models.Model):
    
    group_id=models.AutoField(primary_key=True)
    group_name=models.TextField(help_text='Enter Your username' , max_length=50)
    group_location=models.CharField(help_text='Enter Your group_location' , max_length=50)
    group_Type=models.CharField(help_text='Enter Your group_type' , max_length=50)
    group_describtion=models.TextField(help_text='Enter Your Group_describtion' , max_length=50)

    group_reg_date=models.DateField(auto_now_add=True,null=True)
    
    
    group_upload_image=models.ImageField(help_text='group_upload_image ' , max_length=50,null=True)

    class Meta:
        db_table='admin_group_create_details' 