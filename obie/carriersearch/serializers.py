from django.contrib.auth.models import User, Group
from rest_framework import serializers

from carriersearch.models import State, Policy, Carrier, Offering


class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = ['name', 'id']


class PolicySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Policy
        fields = ['name', 'id']


class CarrierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Carrier
        fields = ['name', 'id']


class OfferingSerializer(serializers.ModelSerializer):
    carrier = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Offering
        fields = ['carrier', 'id']


# class StateSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = State
#         fields = ['name']


class CarrierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrier
        fields = ['name', 'id']


class PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = ['name', 'id']


# class OfferingSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Offering
#         fields = ['policy', 'carrier', 'state']
