from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('sensitive/', views.SensitiveView.as_view(), name='sensitive'),
    path('log/', views.LogRequestView.as_view(), name='log'),
    path('blocked/', views.BlockedIPView.as_view(), name='blocked'),
]
