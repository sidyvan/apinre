from django.db import models
from core.models import Turma

from django.conf import settings

class Menssagem(models.Model):

	criado_em = models.DateTimeField(auto_now_add=True)
	enviado_por = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	turma = models.ManyToManyField(Turma)

	def __str__(self):
		return self.titulo