# Create your viewsets here.
from rest_framework import viewsets

from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """User CRUD operations."""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
