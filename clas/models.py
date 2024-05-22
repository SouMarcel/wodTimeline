from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from django.utils import timezone



# Cria a tabela de Edição
class Edicao(models.Model):
    nome = models.CharField(_("Nome"), max_length=100)
    criado_ts = models.DateTimeField(null=False, blank=False, default=timezone.now)
    atualizado_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("edição")
        verbose_name_plural = _("edições")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Edicao_detail", kwargs={"pk": self.pk})


# Cria a tabela de Livro
class Livro(models.Model):
    nome = models.CharField(_("Nome"), max_length=100, blank=False, null=False)
    edicao = models.ForeignKey(Edicao, verbose_name=_("Edição"), on_delete=models.CASCADE)
    editora = models.CharField(_("Editora"), max_length=100)
    revisao = models.CharField(_("Revisão"), max_length=50)
    isbn = models.CharField(_("ISBN"), max_length=13)  # Adicionado max_length
    criado_ts = models.DateTimeField(null=False, blank=False, default=timezone.now)
    atualizado_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("livro")
        verbose_name_plural = _("livros")

    def __str__(self):
        return f"{self.nome} - {self.edicao.nome}"

    def get_absolute_url(self):
        return reverse("Livro_detail", kwargs={"pk": self.pk})


# Cria a tabela de Disciplinas
class Disciplina(models.Model):
    nome = models.CharField(_("Nome"), max_length=100)
    nivel = models.SmallIntegerField(_("Nível"))
    disciplina = models.CharField(_("Disciplina"), max_length=50)
    descricao = models.TextField(_("Descrição"))
    sistema = models.TextField(_("Sistema"))
    efeito = models.TextField(_("Efeito"))
    criado_ts = models.DateTimeField(null=False, blank=False, default=timezone.now)
    atualizado_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("disciplina")
        verbose_name_plural = _("disciplinas")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Disciplina_detail", kwargs={"pk": self.pk})


# Cria a tabela de Clã
class Cla(models.Model):
    edicao = models.ForeignKey(Edicao, verbose_name=_("Edição"), on_delete=models.CASCADE)
    nome = models.CharField(_("Nome"), max_length=100, blank=False, null=False)
    historia = models.TextField(_("História"))
    mote = models.CharField(_("Mote"), max_length=200)
    aparencia = models.TextField(_("Aparência"))
    refugio = models.TextField(_("Refúgio"))
    cria_persona = models.TextField(_("Criação de Personagens"))
    disciplinas = models.ManyToManyField(Disciplina, verbose_name=_("Disciplinas"))
    organizacao = models.TextField(_("Organização"))
    estereotipos = models.TextField(_("Estereótipos"))
    criado_ts = models.DateTimeField(null=False, blank=False, default=timezone.now)
    atualizado_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("clã")
        verbose_name_plural = _("clãs")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Cla_detail", kwargs={"pk": self.pk})
