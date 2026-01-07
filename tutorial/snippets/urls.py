from django.urls import path
from . import views
urlpatterns = [
    path("snippets/", views.SnippetList.as_view(), name='snippets'),
    path('snippets/<int:pk>', views.SnippetDetail.as_view(), name="snippet-details"),
    path('users/', views.UserList.as_view(), name="user"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-details")
]
