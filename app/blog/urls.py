from blog import views
"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('' , views.home , name='home'),
    path('register' , views.user_register , name='register'),
    path('login' , views.user_login , name='login'),
    path('logout' , views.user_logout , name='logout'),
    path('adminpanel' , views.admin , name ='adminpanel'),

    path('profile' , views.user_profile , name ='profile'),
    path('member', views.member , name='member'),

    # slider -------------------------------------------------------------
    path('sliders', views.slider , name='slider'),
    path('slider_form' , views.slider_form , name ='slider_form'),
    path('slider/update/<int:id>', views.update_slider, name='feature_update'),

    # feature -----------------------------------------------------------
    path('feature' , views.feature , name='feature'),
    path('feature_form' , views.feature_form , name='feature_form'),
    path('feature_view' , views.feature_view , name='feature_view'),
    path('feature/feature_open_view/<int:id>' , views.feature_open_view , name='feature_open_view'),
    path('feature/update/<int:id>', views.update_feature, name='feature_update'),
    path('feature/delete/<int:id>', views.delete_feature, name='feature_delete'),
    path('slider/delete/<int:id>', views.delete_slider, name='slider_delete'),


    # user ------------------------------------------
    path('user_data' , views.user_data , name='user-data'),
    path('user/<int:id>/' , views.user_view , name='user_view'),

    path('user/update/<int:id>/', views.update_user, name='update-user'),
    path('user/delete/<int:id>', views.delete_user, name='delete-user'),
    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





 