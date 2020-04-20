from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from carriersearch.serializers import *

# Create your views here.

# todo: update to ModelViewSets, less vervose, need less boilerplate.
class StateList(APIView):
    """
    view for API endpoint "states/"

    get:
    parameters: 
    Return a list all states.
    """
    def get(self, request):
        states = State.objects.all()
        data = StateSerializer(states, many=True).data
        return Response(data)


class PolicyList(APIView):
    """
    view for API endpoint "policies/"

    get:
    parameters: 
    Return a list all policies.
    """
    def get(self, request):
        policies = Policy.objects.all()
        data = PolicySerializer(policies, many=True).data
        return Response(data)


class CarrierList(APIView):
    """
    view for API endpoint "carriers/"

    get:
    parameters: 
    Return a list all carriers.
    """
    def get(self, request):
        carriers = Carrier.objects.all()
        data = CarrierSerializer(carriers, many=True).data
        return Response(data)




class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows states to be viewed or edited.
    """
    queryset = State.objects.all().order_by('name')
    serializer_class = StateSerializer


class PolicyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows policies to be viewed or edited.
    """
    queryset = Policy.objects.all().order_by('name')
    serializer_class = PolicySerializer


class CarrierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows policies to be viewed or edited.
    """
    queryset = Carrier.objects.all().order_by('name')
    serializer_class = CarrierSerializer


class OfferingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows policies to be viewed or edited.
    """
    queryset = Offering.objects.all().order_by('carrier')
    serializer_class = OfferingSerializer


# get all providers

# get all providers for state
# for provider get all states


