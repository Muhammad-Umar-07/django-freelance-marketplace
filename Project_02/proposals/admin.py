from django.contrib import admin
from .models import Proposal


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('job', 'freelancer', 'bid_amount', 'is_accepted', 'created_at')
    list_filter = ('is_accepted', 'created_at')

# Register your models here.
