<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>Bem vindo na avaliação</h1>
    <p>Esta pagina deve ser a primeira a carregar quando o usuario tentar acessar o endereço</p>
    <hr>
    <h2>Primeira questão [1,5 pontos]</h2>
    <p>
        Crie um formulario abaixo com um campo de input(do tipo number), onde o mesmo deve enviar esse dado para
        o arquivo primeiraQ.php, através do metodo GET.
    </p>
    <p>
        O arquivo primeiraQ.php deve recuperar esse valor e exibir os numeros de 0 ate chegar nesse numero.
    </p>
    <p>
        Obs.: considerar que todos os numeros repassados neste input são positivos.
    </p>
    <hr>
    <h2>Segunda questão [1,5 pontos]</h2>
    <p>
        Crie um formulario abaixo com um campo de input(do tipo number), onde o mesmo deve enviar esse dado para
        o arquivo segundaQ.php, através do metodo POST.
    </p>
    <p>
        O arquivo segundaQ.php deve recuperar esse valor e exibir um texto indicando se o numero é par ou impar e se ele é negativo ou positivo.
    </p>
    <hr>
    <h2>Terceira questão [1,5 pontos]</h2>
    <p>
        Crie um formulario abaixo com um campo de button(do tipo submit) com o nome erro, onde o mesmo deve enviar esse dado para
        o arquivo terceiraQ.php, através do metodo GET.
    </p>
    <p>
        O arquivo terceiraQ.php deve utilizar a função header, para retornar a seguinte status de erro "501 Not Implemented".
    </p>
    <h3>
        Dicas:
    </h3>
    <ol>
        <li>Link sobre a função: <a href="https://www.php.net/manual/pt_BR/function.header.php"> aqui </a></li>
        <li>A primeira linha do Cabeçalho http começa com "HTTP/1.1 200 Ok"</li>
    </ol>
    <hr>
    <h2> Quarta questão [1,5 pontos]</h2>
    <p>
        Crie um formulario abaixo com um campo de input(do tipo text), onde o mesmo deve enviar esse dado para
        o arquivo quartaQ.php, através do metodo POST.
    </p>
    <p>
        O arquivo quartaQ.php deve utilizar a função header, para redirecionar o site para realizar uma pesquisa no site do google.
    </p>
    <h3>
        Dicas:
    </h3>
    <ol>
        <li>Link sobre a função: <a href="https://www.php.net/manual/pt_BR/function.header.php"> aqui </a></li>
        <li>O campo chave valor do http, que indica o redirecionamento de uma pagina é "Location: [caminho_redirecionamento]"</li>
        <li>O google realiaza sua pesquisa através da url "https://www.google.com/search?q=[texto_pesquisa]"</li>
    </ol>
</body>

</html>