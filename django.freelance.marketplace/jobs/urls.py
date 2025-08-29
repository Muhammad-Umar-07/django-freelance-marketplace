from django.urls import path
from . import views


urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('create/', views.JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('<int:pk>/status/', views.JobStatusUpdateView.as_view(), name='job_status'),
]


