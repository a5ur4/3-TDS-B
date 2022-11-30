<?php
$conn = mysqli_connect("localhost","root","Acesso_RR_(35824)","atividade");

echo "******MySqli Conectado*******" . PHP_EOL;
echo "" . PHP_EOL;
echo "" . PHP_EOL;

global $chou;
function menuCadastroAluno()
{
    echo "===Menu Cadastro===" . PHP_EOL;
    $nome = readline("Digite o NOME do aluno: ");
    $turma = readline("Digite a TURMA do aluno: ");
    $curso = readline("Digite o CURSO do aluno: ");
    $mensalidade = readline("Digite a Mensalidade do aluno: ");

    popen('cls', 'w');
    cadastrarAluno($nome, $turma, $curso, $mensalidade);

    echo "Registro realizado com sucesso !!" . PHP_EOL;
    readline("Enter, para continuar");
}

function cadastrarAluno($nome, $turma, $curso, $mensalidade)
{
    global $conn;

    mysqli_query($conn,"INSERT INTO classe values ('$nome', '$turma', '$curso', '$mensalidade')");
}


function ListarAluno()
{
    global $conn;
    $comando_selecao = "SELECT * FROM classe;";
    $select = mysqli_query($conn,$comando_selecao);

    echo "=Lista de Alunos=".PHP_EOL;
    echo "" . PHP_EOL;

    while($linha = mysqli_fetch_assoc($select)){
        echo "NOME: ". $linha['Nome']. PHP_EOL;
        echo "TURMA: ". $linha['Turma']. PHP_EOL;
        echo "Curso: " . $linha['Curso'].PHP_EOL;
        echo "Mensalidade: " . $linha['Mensalidade'].PHP_EOL;
        echo "===============". PHP_EOL;
    }

}

function menuExcluirAluno()
{
    global $conn;
    echo "===Menu Excluir===" . PHP_EOL;
    $nomeExclusão = readline("Digite o NOME do aluno(a) para exclusão: ");

    mysqli_query($conn,"DELETE FROM classe WHERE Nome='$nomeExclusão'");


}

function menuAlterarAluno()
{
    global $conn;
    global $nome;

    echo "=== Menu Alterar ===" . PHP_EOL;

    $nomeUpdate = readline("Digite o nome para a atualização: ");

    $turmaUpdate = readline("Digite a sua nova turma: ");
    $cursoUpdate = readline("Digite o seu novo curso: ");
    $mensalidadeUpdate = readline("Digite o valor da sua mensalidade: ");

    mysqli_query($conn,"UPDATE classe SET " . 
    "Turma = " . "'$turmaUpdate'". "," .
    "Curso = " . "'$cursoUpdate'" . ",".
    "Mensalidade = " . "'$mensalidadeUpdate'" . 
    "WHERE Nome = ". "'$nomeUpdate'" . ";");

    if ($nomeUpdate != $nome){
        echo "Atualização feita" . PHP_EOL;
        readline("Enter, para continuar ");
    } else {
        echo "!!! INVALIDO !!!". PHP_EOL;
        readline("Enter, para continuar ");
    }
}

while($chou != 5){
    echo "==== Menu Aluno ====" . PHP_EOL;
    echo "1 - Cadastrar Aluno" . PHP_EOL;
    echo "2 - Listar os alunos" . PHP_EOL;
    echo "3 - Excluir Aluno" . PHP_EOL;
    echo "4 - Atualizar dados Aluno" . PHP_EOL;
    echo "5 - Sair" . PHP_EOL; 

    $chou = readline("Digite a sua opção: ");
    if ($chou == 1){
        menuCadastroAluno();
    }
    if ($chou ==2 ){
        ListarAluno();
    }
    if ($chou == 3){
        menuExcluirAluno();
    }
    if ($chou == 4){
        menuAlterarAluno();
    }
}
?>