from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username", "email", "password1", "password2",
        )

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Create a basic profile without role-specific details
            profile = Profile.objects.create(
                user=user,
                # Default role to be updated later
                role="",
            )
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'country', 'contact_email',
            # Freelancer fields
            'skills', 'hourly_rate', 'portfolio_url', 'experience', 'languages',
            # Client fields
            'desired_freelancer_type', 'desired_skills', 'budget', 
            'preferred_languages', 'requirements_description',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show only relevant fields based on user role
        if self.instance and self.instance.role == 'freelancer':
            # Hide client fields
            client_fields = ['desired_freelancer_type', 'desired_skills', 'budget', 
                           'preferred_languages', 'requirements_description']
            for field in client_fields:
                if field in self.fields:
                    del self.fields[field]
        elif self.instance and self.instance.role == 'client':
            # Hide freelancer fields
            freelancer_fields = ['skills', 'hourly_rate', 'portfolio_url', 
                               'experience', 'languages']
            for field in freelancer_fields:
                if field in self.fields:
                    del self.fields[field]



