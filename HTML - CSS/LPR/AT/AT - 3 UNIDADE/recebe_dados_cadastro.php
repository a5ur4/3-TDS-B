<?php



$nome = $_GET['nome'];
$endereco = $_GET['endereco'];
$numero = $_GET['numero'];
$bairro = $_GET['bairro'];
$cep = $_GET['cep'];
$estado = $_GET['estado'];
$cidade = $_GET['cidade'];
$habilidades = $_GET['habilidades'];
$genero = $_GET['genero'];
$linguagens = $_GET['lang'];
$arquivo = $_GET['arquivo'];
$cor = $_GET['cor'];
$obs = $_GET['obs'];
$usuario = $_GET["usuario"];
$senha = $_GET["senha"];

 
echo "*************************************<br>";
echo "                 <strong>DADOS DE ACESSO</strong><br>";
echo "*************************************<br>";
echo "<br>$usuario<br>";
echo "<br>$senha<br>";


echo "*************************************<br>";
echo "                 <strong>DADOS RECEBIDOS</strong><br>";
echo "*************************************<br>";


echo "--------------------------------------------------------<br>";
echo "                 <strong>DADOS PESSOAIS</strong><br>";
echo "--------------------------------------------------------<br>";
echo "<br>$nome<br>";
echo "$endereco<br>";
echo "$numero<br>";
echo "$bairro<br>";
echo "$cep<br>";
echo "$estado<br>";
echo "$cidade<br><br>";

echo "--------------------------------------------------------<br>";
echo "                 <strong>HABILIDADES</strong><br>";
echo "--------------------------------------------------------<br>";

echo "<br>";

foreach($habilidades as $habilidade){
   echo "$habilidade<br>";
}

echo "<br>";

echo "--------------------------------------------------------<br>";
echo "                 <strong>GÊNERO</strong><br>";
echo "--------------------------------------------------------<br>";

echo "<br>";
echo "$genero<br><br>";

echo "--------------------------------------------------------<br>";
echo "                 <strong>LINGUAGENS</strong><br>";
echo "--------------------------------------------------------<br>";

echo "<br>";

foreach($linguagens as $lang){
    echo "$lang<br>";
}

echo "<br>";

echo "--------------------------------------------------------<br>";
echo "                 <strong>ARQUIVO</strong><br>";
echo "--------------------------------------------------------<br>";

echo "<br>$arquivo<br><br>";

echo "--------------------------------------------------------<br>";
echo "                 <strong>COR</strong><br>";
echo "--------------------------------------------------------<br>";

echo "<br>$cor<br><br>";

echo "--------------------------------------------------------<br>";
echo "                 <strong>OBSERVAÇÃO</strong><br>";
echo "--------------------------------------------------------<br>";

echo "<br>";

echo "$obs<br><br>";

?>