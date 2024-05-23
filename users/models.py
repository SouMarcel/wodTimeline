from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Edicao(models.Model):
    nome = models.CharField("Nome", max_length=100)  # Nome da edição do jogo
    criado_em = models.DateField("Data de Criação", auto_now_add=True)  # Data de criação da edição (auto preenchida)
    atualizado_em = models.DateField("Data de Atualização", auto_now=True)  # Data de última atualização da edição (auto atualizada)

    class Meta:
        verbose_name = _("edição")
        verbose_name_plural = _("edições")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Edicao_detail", kwargs={"pk": self.pk})
