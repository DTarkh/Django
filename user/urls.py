from django.urls import path
from . import views
from bookshop.urls import urlpatterns

app_name = 'user'

urlpatterns = [
    path('registration/', views.registration, name='registration' ),
    path('logout/', views.Logout, name='logout' ),
]