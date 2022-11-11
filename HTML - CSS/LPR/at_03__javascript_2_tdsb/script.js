function calcularMedia(){
    var nota1 = parseInt(document.getElementById("nota1").value)
    var nota2 = parseInt(document.getElementById("nota2").value)
    var nota3 = parseInt(document.getElementById("nota3").value)
    var nota4 = parseInt(document.getElementById("nota4").value)
    var media = nota1 + nota2 + nota3 + nota4
    var media_final = media / 4
    document.getElementById("media").innerText = "MÉDIA = " + media_final
} 