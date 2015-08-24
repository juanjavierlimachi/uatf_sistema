$(document).ready(inicio)

function crearFormulario(data){
    $("#formulario").html(data);
}
function inicio()
{
    var tbuscar=$("#id_texto").attr('autocomplete','off');
    tbuscar.keypress(buscar);
}
function buscar(){

    $.ajax({
        type:'GET',
        url:'/buscar/',
        data:$("#fbuscar").serialize(),
        success:resultado,
        error:errores
    })
}
function resultado(data){
    $(".resultados").fadeIn("slow");
    $(".resultados").html(data);
}
function errores(){
    alert ("Error");
}
