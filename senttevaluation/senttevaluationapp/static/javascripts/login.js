function validar(){
    var usuario=document.getElementById("#usuario").value;
    var contraseña=document.getElementById("#contrasea").value;

    if(usuario="admin"&&contraseña=="admin")
    {
        alert("Bien");
        setTimeout("location.href='http://localhost:8000/adminInicio'", 0);
    }
    else
    {
        alert("Mal");
    }
}