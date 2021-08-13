from django.urls import path
from . import views

app_name = "task_app"
urlpatterns = [
    path('', views.IndexView.as_view(), name='task'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('book/<int:TaskId>', views.Booking, name="booking"),
    path('revoke/<int:TaskId>', views.Revoke, name="revoking"),
    path('download/<int:TaskId>', views.Download, name="download"),
    path('delete/<int:TaskId>', views.Delete, name="delete"),
    path('new-task/', views.NewTask, name="new_task"),
    path('new-task/upload', views.NewTaskUpload, name="upload_handler"),
]