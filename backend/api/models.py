from django.db import models

# Create your models here.
class Fraud(models.Model):
    """Model definition for Fraud."""
    fraud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    time_reported = models.DateTimeField()
    type = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    ip_adress = models.GenericIPAddressField()

