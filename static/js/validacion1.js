function verificarPassword(){
	pass1=document.getElementById("pass1")
	pass2=document.getElementById("pass2")
    
	if (pass1.value != pass2.value) {
		document.getElementById("error").classList.add("mostrar");
  
		return false;
	} else {
  
	document.getElementById("error").classList.remove("mostrar");
	document.getElementById("ok").classList.remove("ocultar");
	document.getElementById("login").disabled = true;
    setTimeout(function() {
    location.reload();
    }, 3000);
 
    return true;
	}
} 

function mostrarpassword(){
	document.getElementById("contraseña").type="text";
}
	
function ocultarpassword(){
	document.getElementById("contraseña").type="password";
	
}
	
function mostrarpasswordnuevo(){
	document.getElementById("pass1").type="text";
}
	
function ocultarpasswordnuevo(){
	document.getElementById("pass1").type="password";
	
}
	
function mostrarpasswordconfirnuevo(){
	document.getElementById("pass2").type="text";
}
	
function ocultarpasswordconfirnuevo(){
	document.getElementById("pass2").type="password";
	
}