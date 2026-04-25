from django.db import models
class Funcionario(models.Model):

    TIPO_FUNCIONARIO = [
    ('estadual', 'Estadual'),
    ('municipal', 'Municipal'),
    ('terceirizado', 'Terceirizado'),
    ]


    CARGO_ESTADUAL = [
    ('professor', 'Professor/Docente'),
    ('agente', 'Agente de Organização Escolar'),
    ] 

    VINCULO = [
    ('efetivo', 'Efetivo'),
    ('estavel', 'Estável'),
    ('contratado', 'Contratado'),
    ]

    nome = models.CharField("Nome", max_length=200)
    cpf = models.CharField("CPF", max_length=14)
    rg = models.CharField("RG", max_length=12)
    data_nascimento = models.DateField("Data de nascimento")

    cep = models.CharField("CEP", max_length=9, blank=True, null=True)
    rua = models.CharField("Rua", max_length=255, blank=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    estado = models.CharField("Estado", max_length=2, blank=True)

    tipo_funcionario = models.CharField(
    "Tipo de Funcionário",
    max_length=20,
    choices=TIPO_FUNCIONARIO,
    default='municipal'
    )

    cargo_estadual = models.CharField(
    "Cargo Estadual",
    max_length=20,
    choices=CARGO_ESTADUAL,
    blank=True,
    null=True
    )

    vinculo = models.CharField(
    "Vínculo",
    max_length=20,
    choices=VINCULO,
    blank=True,
    null=True
    )

    email = models.EmailField("E-mail")
    telefone = models.CharField("Telefone", max_length=12)

    def __str__(self):
        return self.nome