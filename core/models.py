from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Community(models.Model):
    community_name = models.CharField(max_length=100)
    payroll_code = models.CharField(max_length=50, blank=True)
    ownership = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    slug = AutoSlugField(populate_from='community_name')

    def __str__(self):
        return self.community_name

    class Meta:
        verbose_name_plural = "Communities"
        ordering = ['community_name']

class Person(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(null=True, blank=True, max_length=50)
    payroll_id = models.CharField(null=True, max_length=20)
    community = models.ForeignKey(Community, null=True, on_delete=models.CASCADE, related_name="primary_community")

    class AllocationTypes(models.TextChoices):
        eastern = 'ER', 'Eastern Region'
        central = 'CR', 'Central Region'
        all = 'ALL', 'All Communities'
        community = 'C', 'Home Community'
        all_except_arrow = 'AXA', 'All Communities Except Arrow'
        travel = 'TRV', 'Travel Team'
        new_dev = 'ND', 'New Development'
        manual = 'M', 'Manual'

    allocation_type = models.CharField(max_length=3, choices=AllocationTypes.choices)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = "People"
        ordering = ['user__last_name']
