<?php

static $listaOpcoesValidas = [1, 2, 3, 4, 5];
$AlunosMemory = [];
$opcao = 0;

function pegarIndiceAlunoArrayPelaMatricula($matricaulaBusca)
{
    global $AlunosMemory;
    foreach ($AlunosMemory as $key => $value) {
        if ($value["Matricula"] == $matricaulaBusca) {
            return $key;
        }
    }
    return -1;
}

function CadastrarAluno($nome, $turma, $curso, $matricula)
{
    global $AlunosMemory;
    $AlunosMemory[] = [
        "Nome" => $nome,
        "Turma" => $turma,
        "Curso" => $curso,
        "Matricula" => $matricula
    ];
}

function MenuCadastro()
{
    echo "===Menu Cadastro===" . PHP_EOL;
    $nome = readline("Digite o NOME do aluno: ");
    $turma = readline("Digite a TURMA do aluno: ");
    $curso = readline("Digite o CURSO do aluno: ");
    $matricula = readline("Digite a MATRICULA do aluno: ");

    popen('cls', 'w');
    CadastrarAluno($nome, $turma, $curso, $matricula);

    echo "Registro realizado com sucesso !!" . PHP_EOL;
    readline("Click em qualquer tecla para continuar...");
}

function MenuListar()
{
    global $AlunosMemory;
    echo "===Lista de Alunos===" . PHP_EOL;
    foreach ($AlunosMemory as $aluno) {
        echo "+++++++++++++++++++++++++" . PHP_EOL;
        echo "Nome: " . $aluno['Nome'] . PHP_EOL;
        echo "Turma: " . $aluno['Turma'] . PHP_EOL;
        echo "Curso: " . $aluno['Curso'] . PHP_EOL;
        echo "Matricula: " . $aluno['Matricula'] . PHP_EOL;
    }
    readline("Click em qualquer tecla para continuar... ");
}

function MenuExcluir()
{
    global $AlunosMemory;
    echo "===Menu Excluir===" . PHP_EOL;
    $matriculaExclusão = readline("Digite a matricula do aluno para exclusão: ");

    $resultadoBusca = pegarIndiceAlunoArrayPelaMatricula($matriculaExclusão);
    if ($resultadoBusca == -1) {
        readline("!!!!!  Matricula Invalida !!!!!");
        readline("Click em qualquer tecla para continuar... ");
    } else {
        popen('cls', 'w');
        unset($AlunosMemory[$resultadoBusca]);
        echo "Registro excluido com sucesso !!" . PHP_EOL;
        readline("Click em qualquer tecla para continuar...");
    }
}

function MenuAlterar()
{

    global $AlunosMemory;
    echo "===Menu Alterar===" . PHP_EOL;
    $matriculaExclusão = readline("Digite a matricula do aluno para alteração: ");
    $resultadoBusca = pegarIndiceAlunoArrayPelaMatricula($matriculaExclusão);
    if ($resultadoBusca == -1) {
        echo "!!!!!  Matricula Invalida !!!!!" . PHP_EOL;
        readline("Click em qualquer tecla para continuar... ");
    } else {
        popen('cls', 'w');
        $dadosAntigos = $AlunosMemory[$resultadoBusca];
        $nome = readline("Digite o novo NOME ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Nome'] . " ]: ");
        $turma = readline("Digite a nova TURMA ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Turma'] . " ]: ");
        $curso = readline("Digite o novo CURSO ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Curso'] . " ]: ");
        $matricula = readline("Digite a nova MATRICULA ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Matricula'] . " ]: ");

        $AlunosMemory[$resultadoBusca]['Nome'] = $nome != "" ? $nome : $dadosAntigos['Nome'];
        $AlunosMemory[$resultadoBusca]['Turma'] = $turma != "" ? $nome : $dadosAntigos['Turma'];
        $AlunosMemory[$resultadoBusca]['Curso'] = $curso != "" ? $nome : $dadosAntigos['Curso'];
        $AlunosMemory[$resultadoBusca]['Matricula'] = $matricula != "" ? $nome : $dadosAntigos['Matricula'];
        echo "Registro atualizado com sucesso !!" . PHP_EOL;
        readline("Click em qualquer tecla para continuar...");
    }
}

function verificarOpcaoMenu($opcao)
{
    switch ($opcao) {
        case 1:
            MenuCadastro();
            break;
        case 2:
            MenuListar();
            break;
        case 3:
            MenuExcluir();
            break;
        case 4:
            MenuAlterar();
            break;
        default:
            echo "Erro cód - 001: Não deveria chegar aqui o código" . PHP_EOL;
            break;
    }
}


while ($opcao != 5) {
    echo "====Menu====" . PHP_EOL;
    echo "1 - Cadastrar Aluno" . PHP_EOL;
    echo "2 - Listar os alunos" . PHP_EOL;
    echo "3 - Excluir Aluno" . PHP_EOL;
    echo "4 - Atualizar dados Aluno" . PHP_EOL;
    echo "5 - Sair" . PHP_EOL;

    $opcao = readline("Digite sua opção: ");
    popen('cls', 'w');

    if (!in_array($opcao, $listaOpcoesValidas)) {
        echo "!!!!!  OPÇÃO INVALIDA  !!!!!" . PHP_EOL;
        readline("Click em qualquer tecla para continuar...");
    }

    verificarOpcaoMenu($opcao);
    popen('cls', 'w');
}
