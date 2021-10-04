$(document).ready(function(){
    var btnEliminar = document.querySelectorAll("#btnEliminar");
    btnEliminar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            var name = btn.dataset.name;
            var confirmacion = confirm('¿Está seguro que desea eliminar: ' + name + '?' );
            if(!confirmacion) {
                e.preventDefault();
            }
        });
    });
});