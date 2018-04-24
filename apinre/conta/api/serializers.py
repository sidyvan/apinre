from rest_framework import serializers
from aviso.models import Menssagem
from conta.models import User

class UserSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = User
        fields = ('id','nome')