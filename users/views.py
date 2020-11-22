from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import CustomUser


#register
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'token': AuthToken.objects.create(user)[1],
        })
        


class CustomUserView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()



class CustomUserViewSet(RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'id'

