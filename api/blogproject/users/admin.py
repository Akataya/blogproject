from django.contrib import admin
from .models import Profile, SubscriptionPlan


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile
        list_display = ('user', 'joined', 'is_author')


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    class Meta:
        model = SubscriptionPlan
        list_display = ('name', 'price')
