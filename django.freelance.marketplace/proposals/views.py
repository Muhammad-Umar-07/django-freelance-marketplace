from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from .models import Proposal
from jobs.models import Job


class ApplyToJobView(LoginRequiredMixin, View):
    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id, is_open=True)
        if job.created_by == request.user:
            return redirect('job_detail', pk=job.id)
        Proposal.objects.get_or_create(
            job=job,
            freelancer=request.user,
            defaults={'cover_letter': request.POST.get('cover_letter', ''), 'bid_amount': request.POST.get('bid_amount') or 0},
        )
        return redirect('job_detail', pk=job.id)


class WithdrawProposalView(LoginRequiredMixin, View):
    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        Proposal.objects.filter(job=job, freelancer=request.user).delete()
        return redirect('job_detail', pk=job.id)

from django.shortcuts import render

# Create your views here.
