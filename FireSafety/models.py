from django.db import models
from django.urls import reverse

# Create your models here.


class firesafetyDataset(models.Model):
    id_inset = models.PositiveSmallIntegerField()
    place_name = models.CharField(max_length=128)
    place_address = models.CharField(max_length=128)
    violate_name = models.CharField(max_length=128)
    check_time = models.CharField(max_length=128)
    place_purpose = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse("firesafety:firesafety-detail", kwargs={"id": self.id})