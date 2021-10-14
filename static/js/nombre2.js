function validarformulario(){
    var Username = document.formRegistro.Username;
    var email = document.formRegistro.correo;
    var password = document.formRegistro.password;


    var username_len = Username.value.length;
    
    if (username_len ==0 || username_len<8){
        alert("Debes ingresar un nombre de usuario con minimo 8 Caracteres");
        username.focus();
        return false;
    }
    
    var formato_email = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
    if (!email.value.match(formato_email)){
        alert("Debes ingresar un correo electronico valido");
        email.focus();
        return false;
    }
    var password_len = password.value.length;
    if (password_len ==0 || password_len < 8){
        alert("Debes ingresar una contraseña con minimo 8 Caracteres");
        password.focus();
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

function Validarcontraseñas(){

    password = document.getElementById('password');
    pass2 = document.getElementById('pass2');

}