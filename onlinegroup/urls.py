"""onlinegroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from userapp import views as user_views
from adminapp import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # userviews
    path('',user_views.home,name='home'),
    path('about',user_views.about,name='about'),
    path('contact',user_views.contact,name='contact'),
    path('latest_join_groups',user_views.latest_join_groups,name='latest_join_groups'),
    path('news_feeds',user_views.news_feeds,name='news_feeds'),
    path('user_dashboard',user_views.user_dashboard,name='user_dashboard'),
    path('user_profile',user_views.user_profile,name='user_profile'),
    path('user_latest_join_groups',user_views.user_latest_join_groups,name='user_latest_join_groups'),
    path('user_news_feeds',user_views.user_news_feeds,name='user_news_feeds'),
    path('user_upload_files/<int:id>/',user_views.user_upload_files,name='user_upload_files'),
    path('user_view_accepted_groups',user_views.user_view_accepted_groups,name='user_view_accepted_groups'),
    path('user_registration',user_views.user_registration,name='user_registration'),
    path('user_login',user_views.user_login,name='user_login'),
    path('user_about',user_views.user_about,name='user_about'),
    path('user_contact',user_views.user_contact,name='user_contact'),
    path('user_join_button/<int:id>/',user_views.user_join_button,name='user_join_button'),
    path('user_suggested_join',user_views.user_suggested_join,name='user_suggested_join'),
    path('user_suggested_join_button/<int:id>/',user_views.user_suggested_join_button,name='user_suggested_join_button'),

    
    #adminviews
    path('admin_login',admin_views.admin_login,name='admin_login'),
    path('admindashboard',admin_views.admindashboard,name='admindashboard'),
    path('admin_group_create',admin_views.admin_group_create,name='admin_group_create'),
    path('admin_view_group_details',admin_views.admin_view_group_details,name='admin_view_group_details'),
    path('admin_user_register_request',admin_views.admin_user_register_request,name='admin_user_register_request'),
    path('admin_user_group_join_request',admin_views.admin_user_group_join_request,name='admin_user_group_join_request'),
    path('admin_user_upload_file_request',admin_views.admin_user_upload_file_request,name='admin_user_upload_file_request'),
    path('user_upload_accept/<int:id>/',admin_views.user_upload_accept,name='user_upload_accept'),
    path('user_upload_Rejected/<int:id>/',admin_views.user_upload_Rejected,name='user_upload_Rejected'),
    path('admin_user_group_join_request_accept/<int:id>/',admin_views.admin_user_group_join_request_accept,name='admin_user_group_join_request_accept'),
    path('admin_user_group_join_request_Rejected/<int:id>/',admin_views.admin_user_group_join_request_Rejected,name='admin_user_group_join_request_Rejected'),
    path('admin_user_register_request_accept/<int:id>/',admin_views.admin_user_register_request_accept,name='admin_user_register_request_accept'),
    path('admin_user_register_request_Rejected/<int:id>/',admin_views.admin_user_register_request_Rejected,name='admin_user_register_request_Rejected'),
    path('admin_view_user_feedbacks',admin_views.admin_view_user_feedbacks,name='admin_view_user_feedbacks'),

   
    
    
    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
