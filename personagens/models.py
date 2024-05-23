# personagens/models.py

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from datetime import date
from users.models import Livro

class Personagem(models.Model):
    nome = models.CharField(_("nome"), max_length=100, null=False, blank=False)
    alcunha = models.CharField(_("Alcunha"), max_length=100, blank=True, null=True)
    mote = models.TextField(_("Mote"), blank=True, null=True)
    biografia = models.TextField(_("Biografia"), blank=True, null=True)
    ficha = models.URLField(_("Ficha"), max_length=200, blank=True, null=True)
    nascimento = models.DateField(_("Data de Nascimento"), blank=True, null=True)
    abraco = models.DateField(_("Abraço"), blank=True, null=True)
    morte_final = models.DateField(_("Morte final"), blank=True, null=True)
    geracao = models.PositiveSmallIntegerField(_("Geração"), blank=True, null=True)
    senhor = models.ForeignKey("personagens.Personagem", verbose_name=_("Senhor"), on_delete=models.CASCADE, blank=True, null=True)
    cla = models.ForeignKey('clas.Cla', verbose_name=_("Clã"), on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField('clas.Disciplina', verbose_name=_("Disciplinas"))
    livro = models.ForeignKey(Livro, verbose_name=_("Edição"), on_delete=models.CASCADE, blank=True, null=True)
    criado_em = models.DateTimeField(_("Criado en"), auto_now=False, auto_now_add=True)
    atualizado_em = models.DateTimeField(_("Atualizado em"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Personagem")
        verbose_name_plural = _("Personagens")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Personagem_detail", kwargs={"pk": self.pk})

    @property
    def idade(self):
        if self.morte_final:
            return self.morte_final.year - self.nascimento.year - ((self.morte_final.month, self.morte_final.day) < (self.nascimento.month, self.nascimento.day))
        elif self.nascimento:
            today = date.today()
            return today.year - self.nascimento.year - ((today.month, today.day) < (self.nascimento.month, self.nascimento.day))
        return None
