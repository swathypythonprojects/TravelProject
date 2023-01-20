from . import views
from django.urls import path

urlpatterns = [
    path('',views.demofun,name="demofun")

    # path('add/',views.addition,name="addition")
    # path('about/',views.about,name="about"),
    # path('contact/',views.contact,name="contact")
]