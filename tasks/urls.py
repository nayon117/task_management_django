from django.urls import path
from tasks.views import manager_dashboard, test, user_dashboard

urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard), 
    path('test/', test),
]
