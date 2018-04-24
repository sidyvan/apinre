from rest_framework import serializers
from aviso.models import Menssagem
from conta.models import User
from conta.api.serializers import UserSerializer
from core.api.serializers import TurmaSerializer

class MenssagemSerializer(serializers.ModelSerializer):

	enviado_por = UserSerializer()
	turma = TurmaSerializer(many=True)
	class Meta:
		model = Menssagem
		fields = ('id','titulo','conteudo','turma', 'enviado_por')
