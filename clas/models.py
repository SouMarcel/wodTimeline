# clas/models.py

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from personagens.models import Livro

# Modelo para representar uma disciplina
class Disciplina(models.Model):
    # Nome da disciplina
    nome = models.CharField(_("Nome"), max_length=100)
    # Nível da disciplina
    nivel = models.SmallIntegerField(_("Nível"))
    # Tipo de disciplina
    disciplina = models.CharField(_("Disciplina"), max_length=50)
    # Descrição da disciplina
    descricao = models.TextField(_("Descrição"))
    # Sistema da disciplina
    sistema = models.TextField(_("Sistema"))
    # Efeito da disciplina
    efeito = models.TextField(_("Efeito"), blank=True, null=True)
    # Relacionamento com o livro
    livro = models.ForeignKey(Livro, verbose_name=_("Livro"), on_delete=models.CASCADE, blank=True, null=True)
    # Timestamp de criação
    criado_em = models.DateField(_("Criacao"), auto_now=False, auto_now_add=True)
    # Timestamp de atualização
    atualizado_em = models.DateField(_("Update"), auto_now=True, auto_now_add=False)

    class Meta:
        # Nome singular e plural para o modelo
        verbose_name = _("disciplina")
        verbose_name_plural = _("disciplinas")

    def __str__(self):
        # Representação em string do objeto Disciplina
        return f'{self.nome} - {self.nivel} - {self.livro}'

    def get_absolute_url(self):
        # URL para acessar detalhes de uma disciplina específica
        return reverse("Disciplina_detail", kwargs={"pk": self.pk})

# Modelo para representar um clã
class Cla(models.Model):
    # Nome do clã
    nome = models.CharField(_("Nome"), max_length=100, blank=False, null=False)
    # História do clã
    historia = models.TextField(_("História"), blank=True, null=True)
    apelido = models.CharField(_("Apelido"), max_length=50, blank=True, null=True) # Como o clã é conhecido
    mote = models.CharField(_("Mote"), max_length=200, blank=True, null=True) # Mote do clã
    seita = models.TextField(_("Seita"), blank=True, null=True) # Organização politica
    # Aparência do clã
    aparencia = models.TextField(_("Aparência"), blank=True, null=True)
    # Refúgio do clã
    refugio = models.TextField(_("Refúgio"), blank=True, null=True)
    # Criação de personagens do clã
    cria_persona = models.TextField(_("Criação de Personagens"), blank=True, null=True)
    fraquezas = models.TextField(_("Fraquezas"), blank=True, null=True) # Fraquezas do clã
    organizacao = models.TextField(_("Organização"), blank=True, null=True) # Organização do clã
    antecedentes = models.TextField(_("Antecedentes"), blank=True, null=True) # Antecedentes comuns no clã
    # Estereótipos do clã
    estereotipos = models.TextField(_("Estereótipos"), blank=True, null=True)
    logo = models.ImageField(_("Logo"), upload_to='logo', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    disciplinas = models.ManyToManyField(Disciplina, verbose_name=_("Disciplinas")) # Relacionamento com as disciplinas
    # Relacionamento com o livro
    livro = models.ForeignKey(Livro, verbose_name=_("Livro"), on_delete=models.CASCADE, blank=True, null=True)
    # Timestamp de criação
    criado_em = models.DateField(_("Criado em"), auto_now=False, auto_now_add=True)
    # Timestamp de atualização
    atualizado_em = models.DateField(_("Atualizado em"), auto_now=True, auto_now_add=False)

    class Meta:
        # Nome singular e plural para o modelo
        verbose_name = _("clã")
        verbose_name_plural = _("clãs")

    def __str__(self):
        # Representação em string do objeto Cla
        return f'{self.nome} - {self.livro}'

    def get_absolute_url(self):
        # URL para acessar detalhes de um clã específico
        return reverse("Cla_detail", kwargs={"pk": self.pk})
