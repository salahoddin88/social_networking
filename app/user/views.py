from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import (
    views,
    viewsets,
    response,
    status,
    permissions,
)
from .serializers import (
    UserRegistrationSerializer,
    UserSeializer,
)
from utils.check_email_utils import is_valid_email

class UserRegistrationAPIView(views.APIView):
    """ Register a new user """
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                'message' : 'Registration is successfully completed'
            })
        return response.Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )



class UserListViewSets(viewsets.ModelViewSet):
    """ List user with search viewsets """

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserSeializer
    queryset = get_user_model().objects.exclude(is_superuser=True)
    http_method_names = ['get']

    def get_queryset(self):
        self.queryset = self.queryset.exclude(id=self.request.user.id)
        search = self.request.query_params.get('search')
        filter_kwargs = {
            'is_active' : True
        }
        if search:
            is_email = is_valid_email(search)
            if is_email:
                filter_kwargs['email'] = search
            else:
                filter_kwargs['first_name__icontains'] = search
        return self.queryset.filter(**filter_kwargs)

