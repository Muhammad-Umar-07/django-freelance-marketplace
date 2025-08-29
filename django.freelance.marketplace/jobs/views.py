from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View
from django.shortcuts import redirect, get_object_or_404

from .models import Job


class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return queryset.order_by('-created_at')


class JobDetailView(DetailView):
    model = Job


class ClientRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return hasattr(user, 'profile') and user.profile.role == 'client'


class JobCreateView(LoginRequiredMixin, ClientRequiredMixin, CreateView):
    model = Job
    fields = ['title', 'description', 'budget', 'contact_email', 'status']
    success_url = reverse_lazy('job_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('job_list')

    def test_func(self):
        job = self.get_object()
        return job.created_by == self.request.user


class JobStatusUpdateView(LoginRequiredMixin, ClientRequiredMixin, View):
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk, created_by=request.user)
        new_status = request.POST.get('status')
        if new_status in dict(Job.STATUS_CHOICES):
            job.status = new_status
            job.save(update_fields=['status'])
        return redirect('job_detail', pk=pk)

# Create your views here.
