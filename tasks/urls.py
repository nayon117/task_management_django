from django.urls import path
from tasks.views import show_specific_task, show_tasks

urlpatterns = [
    path('show_tasks/', show_tasks),
    path('show_task/<int:id>', show_specific_task),
]
