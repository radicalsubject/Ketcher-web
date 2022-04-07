from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user_id', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-user_id/', include('rest_framework.urls', namespace= 'rest_framework'))
]

