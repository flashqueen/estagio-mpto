from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)
    abbreviation = models.CharField('Sigla', max_length=2, unique=True)

    def __str__(self):
        return f'{self.name}/{self.abbreviation}'
    