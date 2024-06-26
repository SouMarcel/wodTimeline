from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from livros.models import Livro
from disciplinas.models import Disciplina


# Create your models here.
# Modelo para representar um clã
class Cla(models.Model):
    nome = models.CharField(_("Nome"), max_length=100, blank=False, null=False )# Nome do clã
    historia = models.TextField(_("História"), blank=True, null=True) # História do clã
    apelido = models.CharField(_("Apelido"), max_length=50, blank=True, null=True) # Como o clã é conhecido
    mote = models.CharField(_("Mote"), max_length=200, blank=True, null=True) # Mote do clã
    seita = models.TextField(_("Seita"), blank=True, null=True) # Organização politica
    aparencia = models.TextField(_("Aparência"), blank=True, null=True) # Aparência do clã
    refugio = models.TextField(_("Refúgio"), blank=True, null=True) # Refúgio do clã
    cria_persona = models.TextField(_("Criação de Personagens"), blank=True, null=True) # Criação de personagens do clã
    fraquezas = models.TextField(_("Fraquezas"), blank=True, null=True) # Fraquezas do clã
    organizacao = models.TextField(_("Organização"), blank=True, null=True) # Organização do clã
    antecedentes = models.TextField(_("Antecedentes"), blank=True, null=True) # Antecedentes comuns no clã
    estereotipos = models.TextField(_("Estereótipos"), blank=True, null=True) # Estereótipos do clã
    logo = models.ImageField(_("Logo"), upload_to='logo', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    disciplinas = models.ManyToManyField(Disciplina, verbose_name=_("Disciplinas")) # Relacionamento com as disciplinas
    livro = models.ForeignKey(Livro, verbose_name=_("Livro"), on_delete=models.CASCADE, blank=True, null=True) # Relacionamento com o livro
    criado_em = models.DateField(_("Criado em"), auto_now_add=True) # Timestamp de criação
    atualizado_em = models.DateField(_("Atualizado em"), auto_now=True) # Timestamp de atualização

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
