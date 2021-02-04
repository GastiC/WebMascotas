const expresion = /^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$/i;

function newsletter(e){
    var email = document.getElementById("id_email_newsletter").value;
    if (expresion.test(email)){
        console.log(document.getElementById("id_email_newsletter").value);
        alert("Muchas gracias por suscribirte. En unos momentos recibirás un correo nuestro");}
    else {
        console.log(document.getElementById("id_email_newsletter").value);
    }
}


function contacto(e){
    var email = document.getElementById("id_email").value,
    nombre = document.getElementById("id_nombre").value,
    apellido = document.getElementById("id_apellido").value,
    emailConf = document.getElementById("id_confirmacionEmail").value,
    prefijo = document.getElementById("id_codigoArea").value,
    telefono = document.getElementById("id_telefono").value,
    telefonoAlt = document.getElementById("id_celular").value,
    domicilio = document.getElementById("id_domicilio").value,
    localidad = document.getElementById("id_localidad").value,
    cp = document.getElementById("id_cp").value,
    consulta = document.getElementById("id_consulta").value;

    if (nombre != "" && apellido != "" && expresion.test(email) && expresion.test(emailConf) && prefijo != NaN && telefono != NaN && telefonoAlt != NaN && domicilio != "" && localidad != "" && cp != "" && consulta != ""){
        console.log(document.getElementById("id_email").value);
        alert("Muchas gracias por ponerte en contacto. Pronto estaremos respondiendo a tu consulta");}
    else {
        console.log(document.getElementById("id_email").value);
    }
};

function descripcion_busqueda(){
    elemento_descripcion = document.getElementById('id_descripcion').value
    total = elemento_descripcion.length;
    restante = 150 - total;
    console.log(restante)
    document.getElementById('caracteres_busqueda').innerHTML = `${restante} de 150 caractéres restantes.`; 
};

function descripcion_refugio(){
    elemento_descripcion = document.getElementById('id_descripcion').value
    total = elemento_descripcion.length;
    restante = 300 - total;
    console.log(restante)
    document.getElementById('caracteres_refugio').innerHTML = `${restante} de 300 caractéres restantes.`; 
};


function onresize_body () {
    var foto = document.getElementsByClassName("imagen_banner")[0];
    var fondo = document.getElementsByClassName("fondo_banner")[0];

    if (window.innerWidth > 575) {
        total = foto.clientHeight
        fondo.style.minHeight = total + "px";
    } else { fondo.style.minHeight = 0
     };
};
