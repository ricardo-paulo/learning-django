from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Aluno(models.Model):
    nome = models.CharField(max_length=80)
    turma = models.CharField(max_length=30)
    nota = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        ordering = ["-id"] # Chave primária