from django.shortcuts import render
from proApp.serializer import inventorySerializer,UserSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework import authentication,permissions
from proApp.models import inventoryModel
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class UsercreateView(CreateAPIView):
    serializer_class=UserSerializer

    def perform_create(self, serializer):
        return User.objects.create_user(**serializer.validated_data)

class inventoryCreateListView(CreateAPIView,ListAPIView):
    serializer_class=inventorySerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]

    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    
    filterset_fields = ['stock']
    search_fields = ['name','stock']
    ordering_fields = ['name']


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


    def get_queryset(self):
        return inventoryModel.objects.filter(owner=self.request.user)



class inventoryupdatedeleteretrieveView(DestroyAPIView,UpdateAPIView,RetrieveAPIView):
    serializer_class=inventorySerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
        
    lookup_url_kwarg="id"
    def get_queryset(self):
        return inventoryModel.objects.filter(owner=self.request.user)
