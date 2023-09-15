from django.db import models

class Reserva(models.Model):
    cnpj = models.CharField(max_length=150)
    nome_empresa = models.CharField(max_length=150)
    categoria_empresa = models.CharField(max_length=150)
    #quitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_empresa + " - " + self.cnpj

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    #valor = models.FloatField

