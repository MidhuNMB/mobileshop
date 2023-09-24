"""
URL configuration for mobileshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from mobileshopapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index2/',views.index2),
    path('createuser/',views.createuser),
    path('loginuser/',views.loginuser),
    path('index1/',views.index1),
    path('createac1/',views.createac1),
    path('seller home/',views.sellerHome),
    path('staff home/',views.staffHome),
    path('createsellerac/',views.createsellerac),
    path('createstaffac/',views.createstaffac),
    path('login1/',views.login1),
    path('adminHome/',views.adminHome),
    path('userHome/',views.userHome),
    path('viewseller/',views.viewseller),
    path('sellerpg/',views.sellerpg),
    path('staffpg/',views.staffpg),
    path('delete1/<int:id>',views.delete1),
    path('viewstaff/',views.viewstaff),
    path('delete2/<int:id>',views.delete2),
    path('viewuserprofile/',views.viewuserprofile),
    path('updatesellerac/<int:id>',views.updatesellerac),
    path('update1/<int:id>',views.update1),
    path('update2/<int:id>',views.update2),
    path('updatestaffac/<int:id>',views.updatestaffac),
    path('logout/',views.logout),
    path('viewsellerprofile/',views.viewsellerprofile),
    path('deleteSeller/<int:id>',views.deleteSeller),
    path('viewstaffpro/',views.viewstaffpro),
    path('updateuser/<int:id>',views.updateuser),
    path('updateuserac/<int:id>',views.updateuserac)
   

   
 
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)