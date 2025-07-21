from django.urls import path

from .views import (
    SignUpView,
    UserDeleteView,
    UserListView,
    UserUpdateView,
)

urlpatterns = [
    path("", UserListView.as_view(), name="users_list"),
    path("create/", SignUpView.as_view(), name="users_create"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="users_update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="users_delete"),
]