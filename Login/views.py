from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer, HeroSerializer, CadidateSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import HeroListModel, Candidate
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

 
class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({ 'token': token.key,
                              'user_id': user.pk,
                              'username': user.username,
                              'is_staff': user.is_staff},
                                status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This will call the create method in UserSerializer
            token = Token.objects.get(user=user)  # Retrieve the token for the created user
            return Response({
                'user': {
                    'username': user.username,
                    'token': token.key, 
                       # Access the token here
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class LoginAuth(ObtainAuthToken):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username, 
                'is_staff': user.is_staff
            })
             
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token or user not logged in'}, status=status.HTTP_400_BAD_REQUEST)

    

def homeIndex(response):
    return HttpResponse('<h3>Welcome to Django rest frame Work</h3>')




class HeroView(generics.ListCreateAPIView):
    queryset = HeroListModel.objects.all()
    serializer_class = HeroSerializer



class HeroEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeroListModel.objects.all()
    serializer_class = HeroSerializer



class AddHeroList(generics.ListCreateAPIView):
    queryset = HeroListModel.objects.all()
    serializer_class = HeroSerializer



class CandidateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CadidateSerializer
    def get_queryset(self):
        return self.queryset

    def perform_update(self, serializer):
        serializer.save()
    

class CandidateListView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CadidateSerializer
