from django.urls import path
from polls.views import *

urlpatterns = [
   
    path('users/',UserView.as_view())
]
