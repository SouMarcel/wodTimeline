from django.db import models
from django.urls import reverse
from clas.models import Disciplina, Cla
from users.models import Edicao

class Livro(models.Model):
    nome = models.CharField("Nome", max_length=100)  # Nome do livro
    edicao = models.ForeignKey(Edicao, verbose_name="Edição", on_delete=models.CASCADE)  # Edição do livro
    editora = models.CharField("Editora", max_length=100)  # Editora do livro
    revisao = models.CharField("Revisão", max_length=50, blank=True, null=True)  # Número ou identificação da revisão do livro
    isbn = models.CharField("ISBN", max_length=13, blank=True, null=True)  # Número ISBN do livro
    criado_em = models.DateField("Data de Criação", auto_now_add=True)  # Data de criação do registro (auto preenchida)
    atualizado_em = models.DateField("Data de Atualização", auto_now=True)  # Data de última atualização do registro (auto atualizada)

    class Meta:
        verbose_name = "livro"
        verbose_name_plural = "livros"

    def __str__(self):
        return f"{self.nome} - {self.edicao.nome}"

    def get_absolute_url(self):
        return reverse("Livro_detail", kwargs={"pk": self.pk})

class Personagem(models.Model):
    nome = models.CharField("Nome", max_length=100)  # Nome do personagem
    alcunha = models.CharField("Alcunha", max_length=100, blank=True, null=True)  # Alcunha ou apelido do personagem (opcional)
    mote = models.TextField("Mote", blank=True, null=True)  # Descrição ou mote do personagem (opcional)
    ficha = models.URLField("Ficha", blank=True, null=True)  # URL para a ficha do personagem
    nascimento = models.DateField("Data de Nascimento", blank=True, null=True)  # Data de nascimento do personagem
    cla = models.ForeignKey(Cla, verbose_name="Clã", on_delete=models.CASCADE)  # Clã ao qual o personagem pertence
    disciplinas = models.ManyToManyField(Disciplina, verbose_name="Disciplinas")  # Disciplinas que o personagem possui
    criado_em = models.DateField("Data de Criação", auto_now_add=True)  # Data de criação do registro (auto preenchida)
    atualizado_em = models.DateField("Data de Atualização", auto_now=True)  # Data de última atualização do registro (auto atualizada)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Personagem_detail", kwargs={"pk": self.pk})
