from django.db import models


class Funcionario(models.Model):

    nome = models.CharField("Nome", max_length=200)

    rg = models.CharField("RG", max_length=20)

    cpf = models.CharField("CPF", max_length=14)

    data_nascimento = models.DateField("Data de nascimento")

    endereco = models.CharField("Endereço", max_length=255)

    cidade = models.CharField("Cidade", max_length=100)

    email = models.EmailField("E-mail")

    telefone = models.CharField("Telefone", max_length=20)


    def save(self, *args, **kwargs):
        if self.rg:
            self.rg = self.rg.upper()
        if self.cpf:
            self.cpf = self.cpf.upper()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nome