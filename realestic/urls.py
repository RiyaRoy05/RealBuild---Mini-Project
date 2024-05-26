"""realestic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from realesticapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('common/', views.common),
    path('adminhome/',views.adminhome),
    path('customerhome/',views.customerhome),
    
    
    
    path('login/', views.login),
    path("architect/",views.architect),
    path("designer/",views.designer),
    path("contractor/",views.contractor),
    path('customer/',views.customer),
    
    
    path('adminarchitect', views.adminarchitect),
    path('admindesigner/',views.admindesigner),
    path('admincontractor/',views.admincontractor),
    path('admincustomer/',views.admincustomer),
    path('adminapproveuser/', views.adminapproveuser),
    path('customerrequirement/', views.customerrequirement),
    path('editreq', views.editreq),
    path('account', views.account),
    path('assignarchitect/',views.assignarchitect),
    path('architecthome/',views.architecthome),
    path('architectrequest/', views.architectrequest),
    path('architectaddplan/', views.architectaddplan),
    path('architectplan/', views.architectplan),
    path('customerviewplans/', views.customerviewplans),
    path('customerplan/', views.customerplan),
    path('customerviewplan/', views.customerviewplan),
    path('customerplan/', views.customerplan),
    
    
    path('first/',views.first),
    path('second/',views.second),
    path('third/',views.third),
    path('fourth/',views.fourth),
    path('fifth/',views.fifth),
    
    
    
    path('first1/',views.first1),
    path('second1/',views.second1),
    path('third1/',views.third1),
    path('fourth1/',views.fourth1),
    path('fifth1/',views.fifth1),
    
    
    path('customerplanupdate/',views.customerplanupdate),
    path('feedback/',views.feedback),
    path('viewfeedback/',views.viewfeedback),
    
    path('designerhome/',views.designerhome),
    path('contractorhome/',views.contractorhome),
    path('customerviewdesigner/',views.customerviewdesigner),
    path('customerpassplan/',views.customerpassplan),
    
    
    path('designerrequest/',views.designerrequest),
    path('designeraddvideo/',views.designeraddvideo),
    path('designerviewwork/',views.designerviewwork),
    path('customerdesignrequest/',views.customerdesignrequest),
    path('customervideo/',views.customervideo),
    path('customerselectcontractor', views.customerselectcontractor),
    path('customervideoupdate', views.customervideoupdate),
    path('customerassignwork', views.customerassignwork),
    path('contractorrequest', views.contractorrequest),
    path('contractorreject', views.contractorreject),
    path('contractorapprove', views.contractorapprove), 
    path('contractorprequest', views.contractorprequest), 
    path('moduleimages', views.moduleimages), 
    path('addgallery', views.addgallery), 
    path('designeraddgallery', views.designeraddgallery), 
    path('contractorgallery', views.contractoraddgallery), 
    path('customerviewgal', views.customerviewgal), 
    path('customerwork', views.customerwork), 
    
]
