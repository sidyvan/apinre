from rest_framework import viewsets
from rest_framework.response import Response
from aviso.models import Menssagem
from .serializers import MenssagemSerializer
from rest_framework.filters import SearchFilter
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class MenssagemViewSet(viewsets.ModelViewSet):

    #queryset = Menssagem.objects.all().order_by('-id')
    serializer_class = MenssagemSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('^titulo',)
   # permission_classes = (IsAuthenticated,)
   # authentication_classes = (authentication.TokenAuthentication,)
    
   


    def get_queryset(self):
    	return Menssagem.objects.all().order_by('-id')

    def list(self, request, *args, **kwargs):
    	return super(MenssagemViewSet, self).list(request, *args, **kwargs)

