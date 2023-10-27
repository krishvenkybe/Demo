from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.loginUser, name= "Login"),
    path('logout/', views.logout_user, name= "logout"),
    path('signup/', views.register_user, name="register"),
]