from rest_framework import serializers
from ..models import Profile, SubscriptionPlan
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'is_author')


class SubscriptionPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ('name', 'description', 'price')