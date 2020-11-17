from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Person, games_created, Challanges, points_x_system
from .seralizers import UserSerializer, PersonSerializer, GamesCreatedSerializer, ChallangesSerializer, PointsXSystemSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core import permissions

from rest_framework import filters

# Create your views here.

# @csrf_protect

# class LoginViewSet(viewsets.ViewSet):
#     """Checks email and password and return an auth token """
#     # queryset=User.objects.all()
#     serializer_class= AuthTokenSerializer

#     def create(self,request):
#         """Use the ObtainAuthToken APIView to validate and create a token """

#         return ObtainAuthToken().post(request)

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes = (TokenAuthentication,)
    permissions_classes=(permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)
    filter_backends =(filters.SearchFilter,)
    search_fields=('name','email',)

class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    

class GamesCreatedViewSet(viewsets.ModelViewSet):
    queryset = games_created.objects.all()
    serializer_class= GamesCreatedSerializer

class ChallangesViewSet(viewsets.ModelViewSet):
    queryset = Challanges.objects.all()
    serializer_class= ChallangesSerializer

class PointsXSystemViewSet(viewsets.ModelViewSet):
    queryset = points_x_system.objects.all()
    serializer_class = PointsXSystemSerializer

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return  Response({'message': 'sucesso'})


@csrf_exempt
def login_user(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return  Response(user)
        else:
            # messages.error(request,'Usuario e/ou senha invalidos')
            return  Response({'message': user})
    return 