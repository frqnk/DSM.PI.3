from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('login/', v.login, name='login'),
    path('logout/', v.logout, name='logout'),
    path('signup', v.signup, name='signup'),
]