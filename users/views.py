from django.shortcuts import render
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .models import CustomUser
from .serializers import UserSerializer


#register
class RegisterAPI(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'token': AuthToken.objects.create(user)[1],
        })
        

class CustomUserViewSet(RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'id'


class CustomUserView(ListCreateAPIView):
    
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
