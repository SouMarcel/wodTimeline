# models/models.py

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Modelo para representar uma edição
class Edicao(models.Model):
    # Nome da edição
    nome = models.CharField(_("Nome"), max_length=100)
    # Timestamp de criação
    criado_em = models.DateField(_("Criado em"), auto_now_add=True)
    # Timestamp de atualização
    atualizado_em = models.DateField(_("Atualizado em"), auto_now=True)

    class Meta:
        # Nome singular e plural para o modelo
        verbose_name = _("edição")
        verbose_name_plural = _("edições")

    def __str__(self):
        # Representação em string do objeto Edicao
        return self.nome

    def get_absolute_url(self):
        # URL para acessar detalhes de uma edição específica
        return reverse("Edicao_detail", kwargs={"pk": self.pk})


# Modelo para representar um livro
class Livro(models.Model):
    # Nome do livro
    nome = models.CharField(_("Nome"), max_length=100, blank=False, null=False)
    # Relacionamento com a edição
    edicao = models.ForeignKey(Edicao, verbose_name=_("Edição"), on_delete=models.CASCADE)
    # Nome da editora
    editora = models.CharField(_("Editora"), max_length=100)
    # Revisão do livro (opcional)
    revisao = models.CharField(_("Revisão"), max_length=50, blank=True, null=True)
    # ISBN do livro (opcional)
    isbn = models.CharField(_("ISBN"), max_length=13, blank=True, null=True)
    # Timestamp de criação
    criado_em = models.DateField(_("Criado em"), auto_now_add=True)
    # Timestamp de atualização
    atualizado_em = models.DateField(_("Atualizado em"), auto_now=True)

    class Meta:
        # Nome singular e plural para o modelo
        verbose_name = _("livro")
        verbose_name_plural = _("livros")

    def __str__(self):
        # Representação em string do objeto Livro
        return f"{self.nome} - {self.edicao.nome}"

    def get_absolute_url(self):
        # URL para acessar detalhes de um livro específico
        return reverse("Livro_detail", kwargs={"pk": self.pk})