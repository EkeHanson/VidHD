
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('user/create/', views.CreateAdminView.as_view(), name="create_user"),
    
    path('admins/', views.ListAdminView.as_view(), name="list_admins"),
    path('owners/', views.ListOwnerView.as_view(), name="list_owners"),
    
    path('login/', views.LoginView.as_view(), name='login'),
    
    path('admins/<int:user_id>/', views.AdminRetrieveUpdateDeleteView.as_view(), name="admin_detail"),

    path('owners/<int:user_id>/', views.OwnerRetrieveUpdateDeleteView.as_view(), name="owner_detail"),
]
