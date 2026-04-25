document.addEventListener("DOMContentLoaded", function () {
    console.log("TIPO FUNCIONARIO OK");

    function init() {
        const tipo = document.getElementById("id_tipo_funcionario");
        const cargo = document.getElementById("id_cargo_estadual");
        const vinculo = document.getElementById("id_vinculo");

        if (!tipo || !cargo || !vinculo) return;

        function getRow(field) {
            return field.closest(".form-row") || field.closest(".fieldBox") || field.parentElement.parentElement;
        }

        const cargoRow = getRow(cargo);
        const vinculoRow = getRow(vinculo);

        function toggleCampos() {
            if (tipo.value === "estadual") {
                cargoRow.style.display = "";
                vinculoRow.style.display = "";
            } else {
                cargoRow.style.display = "none";
                vinculoRow.style.display = "none";
                cargo.value = "";
                vinculo.value = "";
            }
        }

        toggleCampos();
        tipo.addEventListener("change", toggleCampos);
    }

    setTimeout(init, 200);
});