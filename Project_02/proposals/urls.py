from django.urls import path
from .views import ApplyToJobView, WithdrawProposalView


urlpatterns = [
    path('<int:job_id>/apply/', ApplyToJobView.as_view(), name='proposal_apply'),
    path('<int:job_id>/withdraw/', WithdrawProposalView.as_view(), name='proposal_withdraw'),
]




