# Generated by Django 4.0.5 on 2022-06-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_useruploadfilemodel_upload_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useruploadfilemodel',
            name='search_rank',
            field=models.CharField(default=0, help_text='upload_user_name', max_length=200),
        ),
    ]
