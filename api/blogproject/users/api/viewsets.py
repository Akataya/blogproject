from ..models import Profile, SubscriptionPlan
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, SubscriptionPlanSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    # List, create, retrieve, update, partial_update, destroy
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    # List, create, retrieve, update, partial_update, destroy
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    # List, create, retrieve, update, partial_update, destroy
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer