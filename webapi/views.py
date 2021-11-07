from django.shortcuts import render
from django.views.generic import View
from webapi.models import Advisors_DB,Booking_DB
import json
from django.http import HttpResponse
# from django.core.serializers import serialize
from webapi.mixins import serializeMixin,HttpResponseMixin
from webapi.utils import is_json
from webapi.forms import UserRegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer,LoginSerializer,BookCallSerializer
from rest_framework import response, status
from rest_framework import status
import jwt
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch') # just use disable to csrf verification
class AdvisorList(HttpResponseMixin,serializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            json_data = json.dumps({'msg': 'User Not Found'})
            return self.render_to_http_resourse(json_data, 404)
        else:
            # json_data = self.serialize([emp, ])
            # return self.render_to_http_response(json_data)
            qs=Advisors_DB.objects.all()
            json_data=self.serialize(qs)
            # status1 = self.render_to_http_resourse(json_data)
            return HttpResponse(json_data,content_type='application/json')

class AdvisorBookedList(HttpResponseMixin,serializeMixin,View):
    def get(self, request,id, *args, **kwargs):
        try:
            user = User.objects.get(id=id)
            print(user)
        except User.DoesNotExist:
            json_data = json.dumps({'msg': 'User Not Found'})
            return self.render_to_http_resourse(json_data, 404)
        else:
            qs1 = Advisors_DB.objects.all()
            json_data1 = self.serialize(qs1)
            qs2 = Booking_DB.objects.all()
            json_data2 = self.serialize(qs2)
            p_data1 = json.loads(json_data1)
            p_data2 = json.loads(json_data2)
            # p_data2.pop('booked_by')
            print(p_data1)
            print(p_data2)
            all_booked = []
            for obj1 in p_data1:
                for obj2 in p_data2:
                    if obj1["Advisor_ID"]==obj2["Advisor_ID"]:
                        obj1.update(obj2)
                        print(obj1)
                        all_booked.append(obj1)
            json_data = json.dumps(all_booked)
            # print(obj1)
            return HttpResponse(json_data, content_type='application/json')

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):

        if serializer.is_valid():
            user = serializer.save()
            # print(serializer.data.get('username'))
            email = UserSerializer(user, context=self.get_serializer_context()).data['email']
            token = jwt.encode({'email': email, }, 'secret', algorithm='HS256')
            # print(serializer)
            return Response({
            "User_id" : serializer.data['id'],
            "Token_jwt" : token,},
            status=status.HTTP_201_CREATED, )
        else:
            return Response({"Error":"400_BAD_REQUEST"} )

class LoginAPI(GenericAPIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        # username = request.data.get('username',None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email,password = password)

        if user:
            serializer = self.serializer_class(user)
            email = UserSerializer(user, context=self.get_serializer_context()).data['email']
            token = jwt.encode({'email': email, }, 'secret', algorithm='HS256')
            return Response({
            "User_id": serializer.data['id'],
            "Token_jwt": token, },
            status=status.HTTP_200_OK, )
        return response.Response({'message':'Invalid credential, try again'},status=status.HTTP_401_UNAUTHORIZED)
        # return response.Response(status=status.HTTP_400_BAD_REQUEST)
class BookCallAdvisor(generics.GenericAPIView):
    serializer_class = BookCallSerializer
    def post(self, request,id,adv_id, *args, **kwargs):
        # advi_id = Advisors_DB.objects.get(adv_id)
        # print(advi_id)
        serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     advi_id = Advisors_DB.objects.get(adv_id=adv_id)
        #     print(advi_id)
        if serializer.is_valid():
            user = serializer.save()
            # print(serializer.data.get('advisor'))
        else:
            return Response({"Error": "400_BAD_REQUEST"})

