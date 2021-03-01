from rest_framework import viewsets
from s_organizer_api.models import User
from s_organizer_api.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer