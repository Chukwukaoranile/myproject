from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register_bug, name='register_bug'),
    path('bug/<int:bug_id>/', views.view_bug, name='view_bug'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('link/', views.bug_link, name='bug_list_link'),
]

