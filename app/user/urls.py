from django.urls import (include, path)
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('list', views.UserListViewSets)

app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', views.UserRegistrationAPIView.as_view(), name='user_registration'),
]
