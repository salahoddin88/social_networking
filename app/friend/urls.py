from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('', views.FriendsListViewSets)

urlpatterns = [
    path('request/', views.FriendRequestAPIView.as_view()),
    path('request/<int:pk>/<str:action>/', views.FriendRequestAPIView.as_view()),
    path('', include(router.urls)),
]
