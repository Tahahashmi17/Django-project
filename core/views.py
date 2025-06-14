from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer
from .tasks import send_welcome_email

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "Welcome to the public API! No authentication needed."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = UserSerializer(request.user)
    return Response({"message": "You are authenticated.", "user": user.data})

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_welcome_email.delay(user.email)  # Background email via Celery
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
