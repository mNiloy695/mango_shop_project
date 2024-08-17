from django.shortcuts import render,redirect

from . import serializers
# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework import status
class UserCreationViewSet(APIView):
    serializer_class=serializers.UserRegistrationSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirmation_link=f'https://mango-shop-project-2.onrender.com/user/activate/{uid}/{token}/'
            subject="Confirmation Mail"

            body=render_to_string('confirmation_mail.html',{'confirmation_link':confirmation_link})
            email=EmailMultiAlternatives(subject,'',to=[user.email])
            email.attach_alternative(body,'text/html')
            email.send()
            return Response('check the your email')
        else:
            return Response(serializer.errors)

def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('https://mniloy695.github.io/mango_shop/login.html')
    else:
        return redirect('https://mniloy695.github.io/mango_shop/registration.html')


#user login viewset

class UserLoginViewSet(APIView):
    serializer_class=serializers.LoginSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username,password=password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id,"is_staff":user.is_staff})
            else:
                return Response({'error':'invalid user'})
        else:
            return Response(serializer.errors)

class UserLogoutViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({'detail':"Successfully logout"})
        
class UserSerializerViewSetForChecking(APIView):
    serializer_class = serializers.UserSerialization
    def get(self, request):
        username = request.query_params.get('username')

        try:
            user = User.objects.get(username=username)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
  

