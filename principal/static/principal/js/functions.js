let formulario = document.getElementById("formulario_contacto");

function formulario_contacto(e) {
    e.preventDefault();
    let elementos = formulario.elements
    for (let i = 0; i < elementos.length; i++) {
        const element = elementos[i].value;
        console.log(element);
    }
    alert("Muchas gracias por contactarte con nosotros")
}

//formulario.addEventListener("submit", formulario_contacto)
