function calcularMedia(){
    var nota1 = parseInt(document.getElementById("nota1").value)
    if(isNaN(nota1)){
        alert("Valor invalido, digite todos os termos")
    }
    var nota2 = parseInt(document.getElementById("nota2").value)
    if(isNaN(nota2)){
        alert("Valor invalido, digite todos os termos")
    }
    var nota3 = parseInt(document.getElementById("nota3").value)
    if(isNaN(nota3)){
        alert("Valor invalido, digite todos os termos")
    }
    var nota4 = parseInt(document.getElementById("nota4").value)
    if(isNaN(nota4)){
        alert("Valor invalido, digite todos os termos")
    }
    var media = nota1 + nota2 + nota3 + nota4
    var media_final = media / 4
    if (isNaN(media_final)){
        media_final = "?"
    }
    document.getElementById("media").innerText = "MÉDIA = " + media_final
} 
