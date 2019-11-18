from rest_framework import serializers
from .models import gate_uid


class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('gate',)


class UidSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('uid',)



