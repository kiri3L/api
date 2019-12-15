from rest_framework import serializers
from .models import gate_uid, Gate


class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('gate_id',)


class GateAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = ('gate_id', )


class UidSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('user_id',)


class GateUidSerializer(serializers.ModelSerializer):
    class Meta:
        model = gate_uid
        fields = ('gate_id', 'user_id')
