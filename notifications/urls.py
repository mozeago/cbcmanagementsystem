from django.urls import path

from notifications import views

urlpatterns=[
    path('',views.index,name="index"),
    path('resetpassword/',views.resetpassword,name="resetpassword"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('dashboard/viewtenants/',views.dashboardTenants,name="tenants"),

]