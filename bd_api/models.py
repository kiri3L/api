from django.db import models


class gate_uid(models.Model):
    gate = models.CharField(max_length=128)
    uid = models.CharField(max_length=128, null=True)


class subscribes(models.Model):
    gate = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()