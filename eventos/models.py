# eventos/models.py

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from locais.models import Local
from livros.models import Livro
from personagens.models import Personagem

class Tempo(models.Model):
    """
    Modelo para representar períodos históricos (eras).
    """

    # Escolhas para o período: a.C (antes de Cristo) e d.C (depois de Cristo)
    PERIODO_CHOICE = (
        ('1', 'a.C'),
        ('2', 'd.C'),
    )

    # Campos do modelo Tempo
    era = models.CharField(_("Era"), max_length=50)  # Nome da era (ex: Era Industrial)
    ano_ini = models.IntegerField(_("Ano de Início"))  # Ano de início do período
    p_ini = models.CharField(_("Período de Início"), max_length=1, choices=PERIODO_CHOICE, null=True, blank=True)  # Período de início (a.C ou d.C)
    ano_fim = models.IntegerField(_("Ano de Fim"))  # Ano de término do período
    p_fim = models.CharField(_("Período de Fim"), max_length=1, choices=PERIODO_CHOICE, null=True, blank=True)  # Período de término (a.C ou d.C)
    descricao = models.CharField(_("Descrição"), max_length=200)  # Descrição do período
    criado_em = models.DateField(_("Criado em"), auto_now_add=True)  # Data de criação do registro
    atualizado_em = models.DateField(_("Atualizado em"), auto_now=True)  # Data de última atualização do registro

    class Meta:
        verbose_name = _("tempo")  # Nome singular para o modelo no admin
        verbose_name_plural = _("tempos")  # Nome plural para o modelo no admin

    def __str__(self):
        return self.era  # Retorna o nome da era como representação textual

    def get_absolute_url(self):
        """
        Retorna o URL absoluto para detalhes deste objeto Tempo.
        """
        return reverse("tempo_detail", kwargs={"pk": self.pk})


class Evento(models.Model):
    """
    Modelo para representar eventos históricos associados a um período (Tempo) específico.
    """

    # Campos do modelo Evento
    nome = models.CharField(_("Nome"), max_length=150, blank=False, null=False)  # Nome do evento
    local = models.ManyToManyField(Local, verbose_name=_("Local"))  # Locais associados ao evento
    livro = models.ManyToManyField(Livro, verbose_name=_("Livro"))  # Livros associados ao evento
    personagem = models.ManyToManyField(Personagem, verbose_name=_("Personagem"))  # Personagens associados ao evento
    resumo = models.CharField(_("Resumo"), max_length=200, blank=False, null=False)  # Resumo do evento
    descricao = models.TextField(_("Descrição"))  # Descrição detalhada do evento
    tempo = models.ForeignKey(Tempo, verbose_name=_("Tempo"), on_delete=models.CASCADE)  # Período histórico ao qual o evento pertence
    criado_em = models.DateField(_("Criado em"), auto_now_add=True)  # Data de criação do registro
    atualizado_em = models.DateField(_("Atualizado em"), auto_now=True)  # Data de última atualização do registro

    class Meta:
        verbose_name = _("evento")  # Nome singular para o modelo no admin
        verbose_name_plural = _("eventos")  # Nome plural para o modelo no admin

    def __str__(self):
        return self.nome  # Retorna o nome do evento como representação textual

    def get_absolute_url(self):
        """
        Retorna o URL absoluto para detalhes deste objeto Evento.
        """
        return reverse("evento_detail", kwargs={"pk": self.pk})
