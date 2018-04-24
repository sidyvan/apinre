from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TurmaSerializer
from core.models import Turma
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class TurmaViewSet(viewsets.ModelViewSet):

    #queryset = Menssagem.objects.all().order_by('-id')
    serializer_class = TurmaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('^nome',)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
   


    def get_queryset(self):
    	return Turma.objects.all().order_by('-id')

    def list(self, request, *args, **kwargs):
    	return super(TurmaViewSet, self).list(request, *args, **kwargs)
