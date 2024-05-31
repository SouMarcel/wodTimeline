from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# from datetime import date
from livros.models import Livro


# Create your models here.
class Local(models.Model):

    DIMENSAO_CHOICE = (
        ('1', 'Terreno'         ),
        ('2', 'Umbra rasa'      ),
        ('3', 'Umbra media'     ),
        ('4', 'Umbra profunda'  ),
        ('5', 'Sonhar proximo'  ),
        ('6', 'Sonha distante'  ),
        ('7', 'Sonhar profundo' ),
        ('8', 'Teia digital'    ),
    )

    nome = models.CharField(_("Nome"), max_length=100)
    regiao = models.CharField(_("Região"), max_length=200, null=True, blank=True)
    dimensao = models.CharField(_("Dimensão"), max_length=3, choices=DIMENSAO_CHOICE, null=True, blank=True)
    era = models.CharField(_("Era"), max_length=100, null=True, blank=True)
    livro = models.ForeignKey(Livro, verbose_name=_("Livro"), on_delete=models.CASCADE)
    criado_em = models.DateField(_("Criado em"), auto_now=False, auto_now_add=True)
    autualizado_em = models.DateField(_("Atualizado em"), auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = _("Local")
        verbose_name_plural = _("Locals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Local_detail", kwargs={"pk": self.pk})