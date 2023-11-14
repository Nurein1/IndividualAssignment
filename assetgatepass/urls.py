from . import views
from django.urls import path

#Url Configuarations
urlpatterns = [
    path('main/', views.main),
    path('sgs/', views.sgs),
    path('security/', views.security),
]