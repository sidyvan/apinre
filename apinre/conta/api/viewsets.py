from rest_framework import viewsets
from rest_framework.response import Response
from conta.models import User
from .serializers import UserSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):

    #queryset = Menssagem.objects.all().order_by('-id')
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('^nome',)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
   


    def get_queryset(self):
    	return User.objects.all().order_by('nome')

    def list(self, request, *args, **kwargs):
    	return super(UserViewSet, self).list(request, *args, **kwargs)

