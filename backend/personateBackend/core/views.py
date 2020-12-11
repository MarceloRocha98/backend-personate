from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Person, games_created, Challanges, points_x_system, system_images
from .seralizers import UserSerializer, PersonSerializer, GamesCreatedSerializer, ChallangesSerializer, PointsXSystemSerializer, system_imagesSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes

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
    permission_classes=(permissions.UpdateOwnProfile,)
    # permissions_classes=(permissions. , IsAuthenticatedOrReadOnly)
    filter_backends =(filters.SearchFilter,)
    search_fields=('username','email',)

class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes=(IsAuthenticatedOrReadOnly)
    

class GamesCreatedViewSet(viewsets.ModelViewSet):
    queryset = games_created.objects.all()
    serializer_class= GamesCreatedSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

class ChallangesViewSet(viewsets.ModelViewSet):
    queryset = Challanges.objects.all()
    serializer_class= ChallangesSerializer
    permission_classes=(permissions.handleChallange, IsAuthenticatedOrReadOnly)
 

class PointsXSystemViewSet(viewsets.ModelViewSet):
    queryset = points_x_system.objects.all()
    serializer_class = PointsXSystemSerializer
    authentication_classes = (TokenAuthentication,)
    # permissions_classes=( IsAuthenticatedOrReadOnly)
    permission_classes=(permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

class system_imagesViewSet(viewsets.ModelViewSet):
    queryset= system_images.objects.all()
    serializer_class = system_imagesSerializer
    authentication_classes=(TokenAuthentication,)
   


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