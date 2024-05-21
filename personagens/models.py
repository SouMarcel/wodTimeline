from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Personagens(models.Model):
    nome = models.CharField("nome",max_length=100, null=False, blank=False)  # Adiciona um campo name ao modelo
    alcunha = models.CharField("alcunha", max_length=100)
    mote = models.TextField
    cla = 
    disciplina = models.ManyToManyField(Disciplina, related_name='personagens')
    ficha = 
    nascimento =
    criacao = 
    

    class Meta:
        verbose_name = _("Personagem")
        verbose_name_plural = _("Personagens")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Personagem_detail", kwargs={"pk": self.pk})  # Ajuste 'Personagem_detail' para corresponder à sua URL real
