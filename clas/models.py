from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Disciplina(models.Model):
    nome = models.CharField("Nome", max_length=100)  # Nome da disciplina
    nivel = models.SmallIntegerField("Nível")  # Nível da disciplina
    disciplina = models.CharField("Disciplina", max_length=50)  # Nome alternativo da disciplina (se houver)
    descricao = models.TextField("Descrição")  # Descrição da disciplina
    sistema = models.TextField("Sistema")  # Detalhes sobre o sistema relacionado à disciplina
    efeito = models.TextField("Efeito")  # Efeito da disciplina
    criado_em = models.DateField("Data de Criação", auto_now_add=True)  # Data de criação do registro (auto preenchida)
    atualizado_em = models.DateField("Data de Atualização", auto_now=True)  # Data de última atualização do registro (auto atualizada)

    class Meta:
        verbose_name = _("disciplina")
        verbose_name_plural = _("disciplinas")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Disciplina_detail", kwargs={"pk": self.pk})

class Cla(models.Model):
    nome = models.CharField("Nome", max_length=100)  # Nome do clã
    historia = models.TextField("História", blank=True, null=True)  # História do clã
    mote = models.CharField("Mote", max_length=200, blank=True, null=True)  # Mote ou lema do clã
    aparencia = models.TextField("Aparência", blank=True, null=True)  # Descrição da aparência característica dos membros do clã
    refugio = models.TextField("Refúgio", blank=True, null=True)  # Descrição do refúgio ou local de residência do clã
    criacao_personagens = models.TextField("Criação de Personagens", blank=True, null=True)  # Diretrizes para a criação de personagens do clã
    organizacao = models.TextField("Organização", blank=True, null=True)  # Estrutura organizacional do clã
    estereotipos = models.TextField("Estereótipos", blank=True, null=True)  # Estereótipos associados ao clã
    disciplinas = models.ManyToManyField(Disciplina, verbose_name="Disciplinas")  # Disciplinas associadas ao clã
    edicao = models.ForeignKey('users.Edicao', verbose_name=_("Edição"), on_delete=models.CASCADE)  # Edição do jogo associada ao clã
    criado_em = models.DateField("Data de Criação", auto_now_add=True)  # Data de criação do registro (auto preenchida)
    atualizado_em = models.DateField("Data de Atualização", auto_now=True)  # Data de última atualização do registro (auto atualizada)

    class Meta:
        verbose_name = _("clã")
        verbose_name_plural = _("clãs")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Cla_detail", kwargs={"pk": self.pk})
