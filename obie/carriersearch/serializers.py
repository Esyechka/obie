from django.contrib.auth.models import User, Group
from rest_framework import serializers

from carriersearch.models import State, Policy, Carrier


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['name']


class CarrierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrier
        fields = ['name']


class PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = ['name']


class CarrierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrier
        fields = ['policy', 'carrier', 'state']
