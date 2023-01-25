from django.urls import path
from django.http import HttpResponse
from profileApp import views

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('education', views.education, name="education"),
    path('insteres', views.insteres, name="insteres"),
    path('idol', views.idol, name="idol"),
    path('sale', views.sale, name="sale"),
    path('ShowData', views.ShowMyData,  name="ShowData")


]