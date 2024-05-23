# personagens/models.py

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from users.models import Livro


# Modelo para representar um personagem
class Personagem(models.Model):
    # Nome do personagem
    nome = models.CharField("nome", max_length=100, null=False, blank=False)
    # Alcunha do personagem
    alcunha = models.CharField("alcunha", max_length=100, blank=True, null=True)
    # Mote do personagem (opcional)
    mote = models.TextField(blank=True, null=True)
    # URL da ficha do personagem
    ficha = models.URLField(_("Ficha"), max_length=200)
    # Data de nascimento do personagem
    nascimento = models.DateField(_("Data de Nascimento"), auto_now=False, auto_now_add=False)
    # Relacionamento com a Clã
    cla = models.ForeignKey('clas.Cla', verbose_name=_("Cla"), on_delete=models.CASCADE)
    # Relacionamento com as disciplinas
    disciplinas = models.ManyToManyField('clas.Disciplina', verbose_name=_("Disciplinas"))
    # Relacionamento com a edição (representada pelo livro)
    livro = models.ForeignKey(Livro, verbose_name=_("Edição"), on_delete=models.CASCADE , blank=True, null=True)
    # Timestamp de criação
    criado_em = models.DateField(_("Criacao"), auto_now=False, auto_now_add=True)
    # Timestamp de atualização
    atualizado_em = models.DateField(_("Update"), auto_now=True, auto_now_add=False)

    class Meta:
        # Nome singular e plural para o modelo
        verbose_name = _("Personagem")
        verbose_name_plural = _("Personagens")

    def __str__(self):
        # Representação em string do objeto Personagem
        return self.nome

    def get_absolute_url(self):
        # URL para acessar detalhes de um personagem específico
        return reverse("Personagem_detail", kwargs={"pk": self.pk})
