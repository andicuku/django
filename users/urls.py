from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserIndexView, UserCreateAsAdminView, UserPasswordView, UserUpdateView, user_delete


app_name = 'users'

urlpatterns =[
    path('', login_required(UserIndexView.as_view()), name='user-index'),
    path('<int:pk>/update/', login_required(UserUpdateView.as_view()), name='user-update'),
    path('<int:pk>/password/', login_required(UserPasswordView.as_view()), name='user-password'),
    path('create/', login_required(UserCreateAsAdminView.as_view()), name='user-create'),
    path('<int:pk>/delete/', login_required(user_delete), name='user-delete'),
]
