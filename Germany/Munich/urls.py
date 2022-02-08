from django.urls import path
from . import views








urlpatterns =[
    path('',views.index,name='index'),
    path('about/',views.about, name='about/'),
    path('navigation/',views.navigation,name='navigation/'),
    path ('available/',views.available, name='available/'),
    path('email/',views.email, name='email/'),
    path('prospects/',views.prospects, name='prospects/'),
    path('newsubscriberinfo/',views.prospects, name='newsubscriberinfo/'),
    ]






    
