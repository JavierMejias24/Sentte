$(document).ready(function(){
    $('#id_Select').addClass('form-select');
    $("#id_Select").val($("#tabla").find("tr").length)
    $("#id_Select").on("change", function() {
        $(this).closest("form").submit()
    })
})