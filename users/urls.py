from django.urls import path

from .views import SignUpView, UserDetailView, UserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', SignUpView.as_view(), name='home'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    # path('login', UserLoginView.as_view(), name='login'),
]
