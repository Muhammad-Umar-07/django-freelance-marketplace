from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.shortcuts import redirect
from .forms import SignupForm, ProfileForm
from .models import Profile


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('setup_profile')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Log the user in automatically
        from django.contrib.auth import login
        login(self.request, self.object)
        return response


class SetupProfileView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'accounts/setup_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user.profile
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Update the role from the form data
        role = request.POST.get('role')
        if role in [choice[0] for choice in Profile.ROLE_CHOICES]:
            self.object.role = role
            self.object.save()
        return super().post(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile


class FreelancerListView(ListView):
    template_name = 'accounts/freelancer_list.html'
    context_object_name = 'freelancers'

    def get_queryset(self):
        return Profile.objects.filter(role='freelancer').select_related('user')


class FreelancerDetailView(DetailView):
    template_name = 'accounts/freelancer_detail.html'
    context_object_name = 'profile'
    model = Profile

# Create your views here.
