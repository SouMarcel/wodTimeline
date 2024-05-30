from django.urls import reverse
from django.db import models
from livros.models import Livro
from django.utils.translation import gettext_lazy as _



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
    livro = models.ForeignKey(Livro, verbose_name=_("Livro"), on_delete=models.CASCADE)
    # Timestamp de criação
    criado_em = models.DateField(_("Criado em"), auto_now_add=True)
    # Timestamp de atualização
    atualizado_em = models.DateField(_("Atualizado em"), auto_now=True)

    class Meta:
        # Nome singular e plural para o modelo
        verbose_name = _("disciplina")
        verbose_name_plural = _("disciplinas")

    def __str__(self):
        # Representação em string do objeto Disciplina
        return f'{self.disciplina} - {self.nivel} - {self.nome} - {self.livro}'

    def get_absolute_url(self):
        # URL para acessar detalhes de uma disciplina específica
        return reverse("Disciplina_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        # Sua lógica personalizada aqui
        self.disciplina = self.disciplina.upper()
        # Chama o método save da superclasse com todos os argumentos recebidos
        super(Disciplina, self).save(*args, **kwargs)

    
    @staticmethod
    def nivel_zero():
        # Retorna todas as disciplinas com nível igual a zero
        return Disciplina.objects.filter(nivel=0)

    @staticmethod
    def nivel_nzero():
        # Retorna todas as disciplinas com nível diferente de zero
        return Disciplina.objects.exclude(nivel=0)