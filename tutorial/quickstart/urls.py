from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# API set to use automagic URL routing
# login URLs included for browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r"^api-auth/", include('rest_framework.urls', namespace='rest_framwork')),
]
