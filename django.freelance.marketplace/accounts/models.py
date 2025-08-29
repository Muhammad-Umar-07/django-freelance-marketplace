from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)

    # Freelancer-specific fields
    skills = models.TextField(blank=True, help_text="Enter up to 5 skills, separated by commas")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    portfolio_url = models.URLField(blank=True)
    experience = models.TextField(blank=True)
    languages = models.CharField(max_length=200, blank=True, help_text="Enter up to 3 languages, separated by commas")

    # Client-specific fields
    desired_freelancer_type = models.CharField(max_length=100, blank=True)
    desired_skills = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    preferred_languages = models.CharField(max_length=200, blank=True, help_text="Enter up to 3 languages, separated by commas")
    requirements_description = models.TextField(blank=True, help_text="Describe the skills and type of person you are looking for")

    def __str__(self) -> str:
        return f"{self.user.username} ({self.role})"
