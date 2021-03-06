$(document).ready(function(){
  //Javascript evaluación
  var btnEvaluacion = document.querySelectorAll("#btnEvaluacion");
  btnEvaluacion.forEach(btn => {
      btn.addEventListener('click', (e) => {
          Swal.fire({
              title: 'Error',
              text: 'Debe esperar que un evaluador le asigne un plan de acción',
              confirmButtonText: 'Esperar',
              icon: 'error'
            })
      })
  })

  //Javascript buscar
  $("#buscar").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#tabla tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  //Javascript eliminar
  var btnEliminar = document.querySelectorAll("#btnEliminar");
  btnEliminar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        var confirmacion = btn.dataset.isConfirmed
        console.log(confirmacion != 'true')
        if (confirmacion != 'true'){
          e.preventDefault()
          var name = btn.dataset.name;
          Swal.fire({
            title: 'Esta seguro que desea eliminar: ' + name + '?',
            showCancelButton: true,
            confirmButtonText: 'Eliminar',
            icon: 'question'
          }).then((result) => {
            if (result.isConfirmed) {
              btn.dataset.isConfirmed = 'true'
              btn.click()
            }
          })
        }
    });
  });
});