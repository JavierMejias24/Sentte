$(document).ready(function(){
    //Mensaje 1
    var btnEvaluacion = document.querySelectorAll("#btnEvaluacion");
    btnEvaluacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            Swal.fire({
                title: 'Error',
                text: 'Debe esperar que se le asigne un plan de acción',
                confirmButtonText: 'Esperar',
                icon: 'error'
            })
        })
    })
})