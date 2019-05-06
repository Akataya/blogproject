from posts.api.viewsets import PostViewSet, CategoryViewSet
from users.api.viewsets import UserViewSet, ProfileViewSet, SubscriptionPlanViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet, base_name='post')
router.register('categories', CategoryViewSet, base_name='category')
router.register('users', UserViewSet, base_name='user')
router.register('profiles', ProfileViewSet, base_name='profile')
router.register('subplans', SubscriptionPlanViewSet, base_name='subplan')
