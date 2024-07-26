from django.db import models

# Create your models here.
# Create your models here.
class Enquiry(models.Model):
    class ServiceRequestChoices(models.TextChoices):
        CLOUD_SERVICES = 'Cloud Services', 'Cloud Services'
        MANAGED_SERVICES = 'Managed Services', 'Managed Services'
        MANAGED_SECURITY_SERVICES = 'Managed Security Services', 'Managed Security Services'
        COLOCATION_SERVICES = 'Colocation Services', 'Colocation Services'
        SOFTWARE_AS_A_SERVICE = 'Software as a Service', 'Software as a Service'
        PLATFORM_AS_A_SERVICE = 'Platform as a Service', 'Platform as a Service'
        OTHER = 'Other', 'Other'

    full_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    business_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    looking_for = models.CharField(max_length=100)
    service_request = models.CharField(
        max_length=100,
        choices=ServiceRequestChoices.choices,
        default=ServiceRequestChoices.OTHER
    )