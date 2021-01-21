from django.db import models
from django.urls import reverse

# Create your models here.


class homepagesDataset(models.Model):
    page_name = models.CharField(max_length=32)