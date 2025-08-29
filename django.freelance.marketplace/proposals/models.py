from django.conf import settings
from django.db import models


class Proposal(models.Model):
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='proposals')
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='proposals')
    cover_letter = models.TextField()
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('job', 'freelancer')

    def __str__(self) -> str:
        return f"{self.freelancer} -> {self.job}"
