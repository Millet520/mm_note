
from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register_view),
    path('login/', views.login_view),
    path('login_out/', views.login_out_view),
]
