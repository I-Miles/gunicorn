from django.db import models

# Create your models here.
# cadastro/models.py
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
