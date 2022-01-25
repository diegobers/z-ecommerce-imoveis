from django.db import models


GRUPO = [
    ('Casa','Casa'),
    ('Apartamento','Apartamento'),
    ('Terreno','Terreno'),
]

TIPO = [
    ('Proprietario','Proprietário'),
    ('Construtora','Construtora'),
    ('Leilao','Leilão'),
]

class Imovel(models.Model):
    descricao = models.CharField(max_length=200, null=True)
    endereco = models.CharField(max_length=200, null=True)
    valor = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    grupo = models.CharField(max_length=20, null=True, choices=GRUPO)   
    tipo = models.CharField(max_length=20, null=True, choices=TIPO)

    def __str__(self):
        return self.descricao 
