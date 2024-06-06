from django.db import models
from django.utils import timezone
import json


class Doacao(models.Model):
    nome = models.CharField(max_length=100)
    data_doacao = models.DateTimeField(default=timezone.now)
    produtos = models.JSONField()  # Armazene os produtos como um campo JSON
    documento = models.CharField(max_length=14)
    local_destino = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if isinstance(self.produtos, str):
            self.produtos = json.loads(self.produtos)
        super().save(*args, **kwargs)
