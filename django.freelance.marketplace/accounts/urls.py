from django.urls import path
from .views import SignupView, ProfileUpdateView, SetupProfileView, FreelancerListView, FreelancerDetailView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/setup/', SetupProfileView.as_view(), name='setup_profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('freelancers/', FreelancerListView.as_view(), name='freelancer_list'),
    path('freelancers/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer_detail'),
]



