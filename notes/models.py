from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.titulo
    
class Nota(models.Model):
    titulo_nota = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    desc_nota = models.TextField()

    def __str__(self) -> str:
        return self.titulo_nota