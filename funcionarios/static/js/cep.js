document.addEventListener("DOMContentLoaded", function () {
    console.log("CEP JS OK");

    const cepField = document.getElementById("id_cep");

    if (cepField) {
        cepField.addEventListener("blur", function () {
            let cep = this.value.replace(/\D/g, '');

            if (cep.length === 8) {
                fetch(`https://viacep.com.br/ws/${cep}/json/`)
                    .then(response => response.json())
                    .then(data => {
                        if (!data.erro) {
                            document.getElementById("id_rua").value = data.logradouro;
                            document.getElementById("id_bairro").value = data.bairro;
                            document.getElementById("id_cidade").value = data.localidade;
                            document.getElementById("id_estado").value = data.uf;
                        }
                    });
            }
        });
    }
});