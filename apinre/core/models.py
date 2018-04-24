from django.db import models

class Setor(models.Model):

	nome = models.CharField(max_length=100)


	def __str__(self):
		return self.nome

class Turma(models.Model):

	nome = models.CharField(max_length=100)
	ativo = models.BooleanField(default=True)


	def __str__(self):
		return self.nome