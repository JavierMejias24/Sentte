$(document).ready(function(){
    const btnEliminar = document.querySelectorAll("#btnEliminar");
    btnEliminar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Está seguro?');
            if(!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();