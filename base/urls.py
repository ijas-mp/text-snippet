from django.conf.urls import url
from django.urls import path, include
from base.views import SnippetList,SnippetUpdate,TagList,listtagdetails

urlpatterns = [
      path('snippet/', SnippetList.as_view()),
      path('snippet/<int:pk>/', SnippetUpdate.as_view()),
      path('tag/',TagList.as_view()),
      path('tag/<int:pk>/',listtagdetails)
]