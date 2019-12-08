from rest_framework import serializers
from .models import gate_uid, Gate


class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('gate',)


class GateAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = ('gate', )


class UidSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('uid',)


class GateUidSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('gate', 'uid')
