"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


app_name = 'main'  # here for namespacing of urls.

router = routers.DefaultRouter()
router.register(r'business', views.BusinessViewSet)

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("test", views.update_coordinates, name="test"),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("view_local/", views.view_local, name="view_local"),
    path("view_local/view_details/", views.venue_details, name="venue_details"),
    #path("api-auth/", include('rest_framework.urls', namespace='rest_framework'))
    path("new_business/", views.new_business, name="new_business"),
    path("user/", views.user, name="user.html"),
    path("update_address", views.update_address, name="update_address"),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
