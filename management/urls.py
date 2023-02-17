from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all, name='all' ),
    path('add', views.add, name='add' ),
    path('dele', views.dele, name='dele' ),
    path('dele/<int:emp_id>', views.dele, name='dele' ),
    path('filter', views.filter, name='filter' ),
]
