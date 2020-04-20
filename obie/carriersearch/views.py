from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from carriersearch.serializers import *
import json

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


class OfferingList(APIView):
    """
    view for API endpoint "carriers/"

    get:
    parameters: 
    Return a list all carriers.
    """
    def get(self, request):
        # todo: handle errors such as misspelled states and policies
        # todo: handle multiple policies, or if only one policy or state is provided
        # todo: handle response via nested drf serializers
        try:
            policy_name = request.query_params.get("policy", None)
            state_name = request.query_params.get("state", None)
            if not policy_name or not state_name:
                raise APIException("incorrect parameters provided")
            policy = Policy.objects.get(name=policy_name.lower())
            state = State.objects.get(name=state_name.upper())
            if policy and state:
                offerings = Offering.objects.filter(state=state, policy=policy)
                carriers = [str(offering.carrier) for offering in offerings]
                # data = OfferingSerializer(offerings, many=True).data
                # return Response(data)
                return JsonResponse(carriers, safe=False)
        except:
            raise APIException("There was a problem!")

 

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


