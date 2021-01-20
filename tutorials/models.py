from django.db import models


class VetOfficers(models.Model):
    name = models.CharField(max_length=150, blank=False, default="")
    county = models.CharField(max_length=150, blank=False, default="")
    published = models.BooleanField(default=False)
    phone_no = models.IntegerField()
    id_no = models.IntegerField(unique=True)
    email = models.EmailField()
