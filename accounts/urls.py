from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('login/', views.login_page_view, name='login'),
    # path('register/', views.register_page_view, name='register'),
    # path('logout/', views.logout_view, name='logout'),


]
