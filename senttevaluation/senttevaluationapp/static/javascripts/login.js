$(document).ready(function validar(){
    var usuario=document.getElementById("usuario").value;
    var contraseña=document.getElementById("contraseña").value;
    if(usuario =="admin")
    {
        if (contraseña == "admin")
        {
            alert("Malo")
           
        }
        else {
            alert("Mal contra");
        }
        alert("Mal usa");
    }
    else
    {
        setTimeout("location.href='http://localhost:8000/adminInicio'", 1000);
    }
});