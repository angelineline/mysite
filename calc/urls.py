from django.urls import path

from . import views

urlpatterns =[
    path('',views.home,name='home'),
   path('',views.login_view,name='login_view')
]