from django.urls import path
from tasks.views import manager_dashboard, test, user_dashboard, create_task

urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard), 
    path('test/', test),
    path('create-task/', create_task)
]
