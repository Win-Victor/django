from django.urls import path

from admins.views import index, UserCreateView, UserListView, UserUpdateView, UserDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:id>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:id>/', UserDeleteView.as_view(), name='admin_users_delete')
]
