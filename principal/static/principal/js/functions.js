const expresion = /^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$/i;

function newsletter() {
    let email = document.getElementById("id_email_newsletter").value;
    if (expresion.test(email)) {
        Swal.fire({
            title: 'Suscripción exitosa',
            text: 'Muchas gracias por suscribirte. En unos momentos recibirás un correo nuestro',
            icon: 'success',
            confirmButtonText: 'Listo',
        })
            .then((result) => {
                if (result.value) {
                    $("#id_newsletter").submit();
                }
            })
    }
    else {
        Swal.fire({
            title: 'Email inválido',
            text: 'Ingrese un correo electrónico válido',
            icon: 'error',
            confirmButtonText: 'Ok',
        })
    }
};

function contacto() {
    let email = document.getElementById("id_email").value,
        nombre = document.getElementById("id_nombre").value,
        apellido = document.getElementById("id_apellido").value,
        emailConf = document.getElementById("id_confirmacionEmail").value,
        prefijo = document.getElementById("id_codigoArea").value,
        telefono = document.getElementById("id_telefono").value,
        telefonoAlt = document.getElementById("id_celular").value,
        domicilio = document.getElementById("id_domicilio").value,
        localidad = document.getElementById("id_localidad").value,
        cp = document.getElementById("id_cp").value,
        consulta = document.getElementById("id_consulta").value,
        boton_contacto = document.getElementById("enviar_contacto");

    if (nombre != "" && apellido != "" && expresion.test(email) && expresion.test(emailConf) && prefijo != "" && telefono != "" && telefono != NaN && telefono <=2147483647 && telefonoAlt != "" && telefonoAlt != NaN && telefonoAlt <=2147483647 && domicilio != "" && localidad != "" && cp != "" && consulta != "") {
        boton_contacto.type = "button"
        Swal.fire({
            title: 'Consulta enviada',
            text: 'Muchas gracias por contactarte con nosotros',
            icon: 'success',
            confirmButtonText: 'Listo',
        })
            .then((result) => {
                if (result.value) {
                    $("#formulario_contacto").submit();
                }
            })
    }
    else {
        boton_contacto.type = "submit";
    }
};

function asociar_refugio() {
    let email = document.getElementById("id_email").value,
        nombre = document.getElementById("id_nombre").value,
        emailConf = document.getElementById("id_confirmacionEmail").value,
        prefijo = document.getElementById("id_codigoArea").value,
        telefono = document.getElementById("id_telefono").value,
        telefonoAlt = document.getElementById("id_celular").value,
        domicilio = document.getElementById("id_direccion").value,
        localidad = document.getElementById("id_localidad").value,
        cp = document.getElementById("id_cp").value,
        provincia = document.getElementById("id_provincia").value,
        descripcion = document.getElementById("id_descripcion").value,
        boton_refugio = document.getElementById("enviar_refugio");
        inputFoto = document.getElementById("id_foto");
        errorEmailDuplicado = document.getElementById("error_1_id_email");        

    if (nombre != "" && expresion.test(email) && expresion.test(emailConf) && prefijo != "" && telefono != "" && telefono != NaN && telefono <=2147483647 && telefonoAlt <=2147483647 && domicilio != "" && localidad != "" && provincia != "" && cp != "" && descripcion != "" ) {
        boton_refugio.type = "button"
        Swal.fire({
            title: 'Refugio asociado',
            text: 'Muchas gracias por asociar tu refugio',
            icon: 'success',
            confirmButtonText: 'Listo',
        })
            .then((result) => {
                if (result.value) {
                    $("#formulario_refugio").submit();
                }
            })
    }
    else {
        boton_refugio.type = "submit";
    }
};


function subir_busqueda() {
    let nombre = document.getElementById("id_nombreMascota").value,
        categoria = document.getElementById("id_categoria").value
        raza = document.getElementById("id_raza").value,
        prefijo = document.getElementById("id_codigoArea").value,
        telefono = document.getElementById("id_telefono").value,
        telefonoAlt = document.getElementById("id_celular").value,
        localidad = document.getElementById("id_localidad").value,
        cp = document.getElementById("id_cp").value,
        provincia = document.getElementById("id_provincia").value,
        descripcion = document.getElementById("id_descripcion").value,
        boton_busqueda = document.getElementById("enviar_busqueda");

    if (nombre != "" && categoria != "" && raza != "" && prefijo != "" && telefono != "" && telefono != NaN && telefono <=2147483647 && telefonoAlt <=2147483647 && localidad != "" && provincia != "" && cp != "" && descripcion != "") {
        boton_busqueda.type = "button"
        Swal.fire({
            title: 'Búsqueda registrada',
            text: 'Tu búsqueda fue publicada exitosamente',
            icon: 'success',
            confirmButtonText: 'Listo',
        })
            .then((result) => {
                if (result.value) {
                    $("#formulario_busqueda").submit();
                }
            })
    }
    else {
        boton_busqueda.type = "submit";
    }
};

function descripcion_busqueda() {
    elemento_descripcion = document.getElementById('id_descripcion').value
    total = elemento_descripcion.length;
    restante = 150 - total;
    console.log(restante)
    document.getElementById('caracteres_busqueda').innerHTML = `${restante} de 150 caractéres restantes.`;
};

function descripcion_refugio() {
    elemento_descripcion = document.getElementById('id_descripcion').value
    total = elemento_descripcion.length;
    restante = 300 - total;
    console.log(restante)
    document.getElementById('caracteres_refugio').innerHTML = `${restante} de 300 caractéres restantes.`;
};


function onresize_body() {
    //Resize del banner

    let foto = document.getElementsByClassName("imagen_banner")[0];
    let fondo = document.getElementsByClassName("fondo_banner")[0];

    if (window.innerWidth <= 575) {
        fondo.style.minHeight = 0;
    } else if (window.innerWidth >= 576) {
        total = foto.clientHeight
        fondo.style.minHeight = total + "px";
    }

    //Resize del contenedor de la foto de los refugios

    let card_descripcion = document.getElementsByClassName("card_descripcion")[0];
    let contenedor_foto = document.getElementsByClassName("contenedor_imagen_refugio")[0];

    if (window.innerWidth < 1200) {
        contenedor_foto.style.minHeight = 0;
    } else if (window.innerWidth >= 1200) {
        if (card_descripcion.clientHeight > contenedor_foto.clientHeight) {
            total = card_descripcion.clientHeight
            contenedor_foto.style.minHeight = total + "px";
            console.log("1")
        } else if (card_descripcion.clientHeight < contenedor_foto.clientHeight) {
            total = contenedor_foto.clientHeight
            card_descripcion.style.minHeight = total + "px";
            console.log("2")
        }


    }


};



