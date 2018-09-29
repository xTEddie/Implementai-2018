from django.urls import path
from .views.user import UserList


urlpatterns = [
    path(r'users', UserList.as_view())
]
