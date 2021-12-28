from django.urls import path
from . import views

urlpatterns=[path("",views.projects_index,name="projects_index"),
path("<int:pk>/",views.project_details,name="project_details"),
path("likeprojects/<int:pk>",views.likeproject,name="likeprojects")]