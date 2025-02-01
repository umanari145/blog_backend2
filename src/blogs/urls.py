from django.urls import include, path
from rest_framework import routers
from blogs import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogsViewSet)
router.register(r'labels', views.LabelsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
