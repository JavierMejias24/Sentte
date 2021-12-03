$(document).ready(function(){
    var btnEvaluacion2 = document.querySelectorAll("#btnEvaluacion2");
    btnEvaluacion2.forEach(btn2 => {
        btn2.addEventListener('click', (e) => {
            Swal.fire({
                title: 'Error',
                text: 'Debe esperar que el evaluador termine de evaluarlo',
                confirmButtonText: 'Esperar',
                icon: 'error'
            })
        })
    })
})