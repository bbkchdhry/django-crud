from django.db import models

# Create your models here.


class Organization(models.Model):
    org_name = models.CharField(max_length=30, blank=True, null=True)
    org_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'Organization'


class Department(models.Model):
    organization = models.ForeignKey(Organization, related_name='departments', on_delete=models.CASCADE, db_column='organization_id')
    dept_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'Department'
