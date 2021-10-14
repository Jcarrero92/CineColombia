function Validarcontraseñas(){
    
var p1 = document.getElementById("password").value;
var p2 = document.getElementById("pass2").value;    



var espacios = false;
var cont = 0;

while (!espacios && (cont < p1.length)) {
if (p1.charAt(cont) == " ")
    espacios = true;
    cont++;
}
    
if (espacios) {
    alert ("La contraseña no puede contener espacios en blanco");
    return false;
}
if (p1.length == 0 || p2.length == 0) {
    alert("Los campos de la password no pueden quedar vacios");
    return false;
}
if (p1 != p2) {
    alert("Las passwords deben de coincidir");
    return false;
} else {
    alert("Todo esta correcto");
    return true; 
}
}

function mostrarpassword(){
    document.getElementById("password").type="text";
}

function ocultarpassword(){
    document.getElementById("password").type="password";

}

function mostrar_password(){
    document.getElementById("pass2").type="text";
}

function ocultar_password(){
    document.getElementById("pass2").type="password";

}