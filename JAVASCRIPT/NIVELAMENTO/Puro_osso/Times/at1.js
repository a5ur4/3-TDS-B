function tenis (){
    let resultado1 = document.getElementById("1").value;
    let resultado2 = document.getElementById("2").value;
    let resultado3 = document.getElementById("3").value;
    let resultado4 = document.getElementById("4").value;
    let resultado5 = document.getElementById("5").value;
    let resultado6 = document.getElementById("6").value;
    let resultados = [resultado1, resultado2, resultado3, resultado4, resultado5, resultado6];
    let counter = 0;
    for (let i = 0; i < resultados.length; i++) {
        if (resultados[i] === 'v') counter++;
    };
    if (counter== 6 || counter == 5){
        let resposta = document.querySelector('#resposta');
        resposta.innerText = 1;
    }
    if (counter== 3 || counter == 4){
        let resposta = document.querySelector('#resposta');
        resposta.innerText = 2;
    }
    if (counter== 1 || counter == 2){
        let resposta = document.querySelector('#resposta');
        resposta.innerText = 3;
    }
    if (counter== 0){
        let resposta = document.querySelector('#resposta');
        resposta.innerText = -1;
    }


}