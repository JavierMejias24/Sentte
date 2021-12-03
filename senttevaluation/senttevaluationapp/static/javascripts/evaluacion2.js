$(document).ready(function(){
    var btnEvaluacion1 = document.querySelectorAll("#btnEvaluacion1");
    btnEvaluacion1.forEach(btn1 => {
        btn1.addEventListener('click', (e) => {
            Swal.fire({
                title: 'Error',
                text: 'Debe esperar que el empleado se autoevalue',
                confirmButtonText: 'Esperar',
                icon: 'error'
            })
        })
    })
})