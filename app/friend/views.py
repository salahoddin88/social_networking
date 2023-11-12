from rest_framework import (
    views,
    viewsets,
    permissions,
    status,
    response,
)
from rest_framework.generics import get_object_or_404
from django.db.models import Q
from friend.models import Friend, FriendRequest
from .serializers import FriendRequestSerializer, FriendListSerializer


class FriendRequestAPIView(views.APIView):
    """ Friend request API View """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = FriendRequestSerializer

    def get(self, request, pk=None):
        """ List all the pending friend request """
        queryset = FriendRequest.objects.filter(
            receiver=request.user,
            status="pending"
        )
        serializer = FriendRequestSerializer(
            queryset,
            many=True,
        )
        return response.Response(serializer.data)

    def post(self, request, pk=None):
        """ Send friend request """
        serializer = FriendRequestSerializer(
            data=request.data,
            context = { 'sender' : request.user },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(
            sender=request.user,
            status="pending"
        )
        return response.Response({
            'message' : 'Friend request send'
        })

    def put(self, request, pk=None, action=None):
        """
            Accept/Reject friend request
            pk : int primary key of friend request
            action: str accept/reject
        """
        if not pk and not action:
            return response.Response({
                'message' : 'bad request'
            }, status=status.HTTP_400_BAD_REQUEST)

        if action not in ['accept', 'reject']:
            return response.Response({
                'message' : 'bad request'
            }, status=status.HTTP_400_BAD_REQUEST)

        filtered_queryset = FriendRequest.objects.filter(
            pk=pk,
            status="pending"
        )
        queryset = get_object_or_404(filtered_queryset, pk=pk)
        queryset.status = action
        queryset.save()
        if action == 'accept':
            Friend.objects.create(
                user_one=queryset.sender,
                user_two=queryset.receiver,
            )
        return response.Response({
            'message' : f'Friend request {action}ed'
        })


class FriendsListViewSets(viewsets.ViewSet):
    """ Friends list """
    queryset = Friend.objects.all()
    serializer_class = FriendListSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request):
        queryset = self.queryset.filter(
            Q(user_one=request.user) | Q(user_two=request.user)
        )
        serializer = self.serializer_class(
            queryset,
            context={ 'user' : request.user },
            many=True
        )
        return response.Response(serializer.data)