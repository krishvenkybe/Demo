from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.loginUser, name= "Login"),
    path('logout/', views.logoutUser, name= "logout"),
]