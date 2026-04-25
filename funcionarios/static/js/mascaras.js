document.addEventListener("DOMContentLoaded", function () {

    const cpf = document.getElementById("id_cpf");
    const rg = document.getElementById("id_rg");

    function mascaraCPF(valor) {
        valor = valor.replace(/\D/g, "");
        valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
        valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
        valor = valor.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
        return valor;
    }

    function mascaraRG(valor) {
        valor = valor.replace(/\D/g, "");
        valor = valor.replace(/(\d{2})(\d)/, "$1.$2");
        valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
        valor = valor.replace(/(\d{3})(\d{1})$/, "$1-$2");
        return valor;
    }

    if (cpf) {
        cpf.addEventListener("input", function () {
            this.value = mascaraCPF(this.value);
        });
    }

    if (rg) {
        rg.addEventListener("input", function () {
            this.value = mascaraRG(this.value);
        });
    }

});