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
