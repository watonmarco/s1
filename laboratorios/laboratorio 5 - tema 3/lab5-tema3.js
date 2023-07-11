function generar() {
    let longitud = document.getElementById("longitud").value;
    let incluirMayus = document.getElementById("mayus").checked; 
    let incluirMinus = document.getElementById("minus").checked; 
    let incluirNum = document.getElementById("num").checked; 
    let incluirEsp = document.getElementById("esp").checked; 
    let contraseña = generarRandom(longitud,incluirMayus,incluirMinus,incluirNum,incluirEsp);
    document.getElementById("contraseña").textContent = "Contraseña Generada: " + contraseña;
}

function generarRandom(longitud, incluirMayus, incluirMinus, incluirNum, incluirEsp) {
    let caracteres = "";
    if (incluirMayus) caracteres = caracteres + "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (incluirMinus) caracteres = caracteres + "abcdefghijklmnopqrstuvwxyz";
    if (incluirNum) caracteres = caracteres + "0123456789";
    if (incluirEsp) caracteres = caracteres + ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~';
    let contraseña = "";
    for (let i = 0; i < longitud; i++) {
        let caracterRandom = caracteres.charAt(Math.floor(Math.random() * caracteres.length));
        contraseña = contraseña + caracterRandom;
    }
    return contraseña;
}