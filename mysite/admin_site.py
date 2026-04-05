from django.contrib.admin import AdminSite

class FuncionarioAdminSite(AdminSite):
    site_header = "Sistema de Cadastro de Funcionários"
    site_title = "Sistema de Cadastro de Funcionários"
    index_title = "Administração do Site"

admin_site = FuncionarioAdminSite(name="func_admin")