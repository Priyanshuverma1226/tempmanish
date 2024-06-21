from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload_csv', views.upload_csv, name='upload_csv'),
    path('my_ticket', views.my_ticket, name='my_ticket'),
    path('ticket', views.ticket, name='ticket'),
  
]
app_name="app"
