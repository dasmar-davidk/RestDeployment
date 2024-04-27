from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProfileSerializer

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World! Это закрытая '}
        return Response(content)

class OpenView(APIView):
    permission_classes = []

    def get(self, request):
        content = {'message': 'Hello, World! Это открытая '}
        return Response(content)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            data = {
            "user_id": user.id,
            "message": "User registered successfully."
        }
            return Response(data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)