# Generated by Django 4.0.5 on 2022-06-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_useruploadfilemodel_upload_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploadfilemodel',
            name='upload_group_type',
            field=models.CharField(help_text='upload_user_name', max_length=200, null=True),
        ),
    ]