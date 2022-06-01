from django.urls import path
from . import views


app_name = 'calculation'
urlpatterns = [
    # path('', views.calculate_mean, name='index'),
    path('', views.calculate_mean, name='index'),
    path('reset_session', views.reset_session, name='reset_session')

]