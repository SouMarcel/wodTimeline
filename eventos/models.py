from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from locais.models import Local
from livros.models import Livro
from personagens.models import Personagem

# Create your models here.
class Evento(models.Model):

    nome = models.CharField(_("Nome"), max_length=150, blank=False, null=False)
    local = models.ManyToManyField(Local, verbose_name=_("Local"))
    livro = models.ManyToManyField(Livro, verbose_name=_("Livro"))  
    personagem = models.ManyToManyField(Personagem, verbose_name=_("Personagem"))
    resumo = models.CharField(_("Resumo"), max_length=200, blank=False, null=False)
    descricao = models.TextField(_("Descrição"))

    class Meta:
        verbose_name = _("evento")
        verbose_name_plural = _("eventos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("evento_detail", kwargs={"pk": self.pk})
