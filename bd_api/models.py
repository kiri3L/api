from django.db import models


class gate_uid(models.Model):
    gate_id = models.CharField(max_length=128)
    uid = models.CharField(max_length=128, null=True)


class Gate(models.Model):
    gate_id = models.CharField(max_length=128, null=False, unique=True)

