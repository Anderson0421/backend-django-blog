from rest_framework import routers
from .api import PostViewSet

router = routers.DefaultRouter()


router.register('api/posts/v1',PostViewSet, 'posts')


urlpatterns = router.urls