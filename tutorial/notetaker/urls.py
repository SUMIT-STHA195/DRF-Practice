from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

note_list = views.NoteViewSet.as_view({"get": "list", "post": "create"})
note_detail = views.NoteViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"})
user_list = views.UserViewSet.as_view({"get": "list"})
user_detail = views.UserViewSet.as_view({"get": "retrieve"})
urlpatterns = format_suffix_patterns(
    [
        path('notes/', note_list, name='note-list'),
        path('notes/<int:pk>/', note_detail, name='note-detail'),
        path('users/', user_list, name='user-list'),
        path('users/<int:pk>', user_detail, name='user-detail')
    ]
)
# without ViewSet
# urlpatterns = format_suffix_patterns(
#     [
#         path('notes/', views.NoteList.as_view(), name='note-list'),
#         path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
#         path('users/', views.UserList.as_view(), name='user-list'),
#         path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail')
#     ]
# )
