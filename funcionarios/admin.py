from django.contrib import admin
from .models import Funcionario
from mysite.admin_site import admin_site


@admin.register(Funcionario, site=admin_site)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "tipo_funcionario", "cidade", "telefone")
    search_fields = ("nome", "cpf", "rg")

    class Media:  # 👈 tem que estar DENTRO da classe
        js = ('js/cep.js', 'js/funcionario.js', 'js/mascaras.js',)
        css = {
            'all': ('admin/css/custom_admin.css',)
        }