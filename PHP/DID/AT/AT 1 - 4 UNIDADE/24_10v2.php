<?php

static $listaOpcoesValidas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$AlunosMemory = [];
$ProfessorMemory = [];
$opcao = 0;
$enter = 0;

function pegarIndiceProfessorArrayPeloNome($nomeProfbusca)
{
    global $ProfessorMemory;
    foreach ($ProfessorMemory as $key => $value) {
        if ($value['Nome_prof'] == $nomeProfbusca) {
            return $key;
        }
    }
}

function pegarIndiceAlunoArrayPeloNome($nomebusca)
{
    global $AlunosMemory;
    foreach ($AlunosMemory as $key => $value) {
        if ($value['Nome'] == $nomebusca) {
            return $key;
        }
    }
    return -1;
}

function CadastrarAluno($nome, $turma, $curso, $mensalidade)
{
    global $AlunosMemory;
    $AlunosMemory[] = [
        "Nome" => $nome,
        "Turma" => $turma,
        "Curso" => $curso,
        "Mensalidade" => $mensalidade
    ];
}

function CadastrarProfessor($nome_prof, $salario_prof)
{
    global $ProfessorMemory;
    $ProfessorMemory[] = [
        "Nome_prof" => $nome_prof,
        "Salario" => $salario_prof
    ];
}

function MenuCadst_prof()
{
    echo "===Menu Cadastro===" . PHP_EOL;
    $nome_prof = readline("Digite o NOME do professor: ");
    if ($nome_prof == null) {
        echo "O nome não pode ser nulo, tente novamente" . PHP_EOL;
        MenuCadst_prof();
    }
    $salario_prof = readline("Digite o SALÁRIO do professor: ");

    popen('cls', 'w');
    CadastrarProfessor($nome_prof, $salario_prof);
    readline("Click na tecla 'Enter' para continuar...");
}

function MenuCadastro()
{
    echo "===Menu Cadastro===" . PHP_EOL;
    $nome = readline("Digite o NOME do aluno: ");
    if ($nome == null) {
        echo "O nome não pode ser nulo, tente novamente" . PHP_EOL;
        MenuCadastro();
    }
    $turma = readline("Digite a TURMA do aluno: ");
    $curso = readline("Digite o CURSO do aluno: ");
    $mensalidade = readline("Digite a MENSALIDADE do aluno: ");

    popen('cls', 'w');
    CadastrarAluno($nome, $turma, $curso, $mensalidade);
    readline("Click na tecla 'Enter' para continuar...");
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
        echo "Mensalidade: R$" . $aluno['Mensalidade'] . PHP_EOL;
    }
    readline("Click na tecla 'Enter' para continuar...");
}

function MenuListar_prof()
{
    global $ProfessorMemory;
    echo "===Lista de Professores===" . PHP_EOL;
    foreach ($ProfessorMemory as $professor) {
        echo "+++++++++++++++++++++++++" . PHP_EOL;
        echo "Nome: " . $professor['Nome_prof'] . PHP_EOL;
        echo "Salário: R$" . $professor['Salario'] . PHP_EOL;
    }
    readline("Click na tecla 'Enter' para continuar...");
}

function MenuExcluir()
{
    global $AlunosMemory;
    echo "===Menu Excluir===" . PHP_EOL;
    $nomeExclusão = readline("Digite o nome do aluno para exclusão: ");

    $resultadoBusca = pegarIndiceAlunoArrayPeloNome($nomeExclusão);
    if ($resultadoBusca == -1) {
        readline("!!!!!  Nome Invalido !!!!!");
        $enter = readline("Click na tecla 'Enter' para continuar...");
        if ($enter != null) {
            echo "Isso não é uma opção invalida" . PHP_EOL;
            exit;
        }
    } else {
        popen('cls', 'w');
        unset($AlunosMemory[$resultadoBusca]);
        echo "Registro excluido com sucesso !!" . PHP_EOL;
        readline("Click na tecla 'Enter' para continuar...");
    }
}

function MenuExcluir_prof()
{
    global $ProfessorMemory;
    echo "===Menu Excluir===" . PHP_EOL;
    $nomeExclusão = readline("Digite o nome do professor para exclusão: ");

    $resultadoBusca = pegarIndiceProfessorArrayPeloNome($nomeExclusão);
    if ($resultadoBusca == -1) {
        readline("!!!!!  Nome Invalido !!!!!");
        readline("Click na tecla 'Enter' para continuar...");
    } else {
        popen('cls', 'w');
        unset($ProfessorMemory[$resultadoBusca]);
        echo "Registro excluido com sucesso !!" . PHP_EOL;
        readline("Click na tecla 'Enter' para continuar...");
    }
}

function MenuAlterar()
{

    global $AlunosMemory;
    echo "===Menu Alterar===" . PHP_EOL;
    $nomeExclusão = readline("Digite o nome do aluno para alteração: ");
    $resultadoBusca = pegarIndiceAlunoArrayPeloNome($nomeExclusão);
    if ($resultadoBusca == -1) {
        echo "!!!!!  Nome Invalido !!!!!" . PHP_EOL;
        readline("Click na tecla 'Enter' para continuar...");
    } else {
        popen('cls', 'w');
        $dadosAntigos = $AlunosMemory[$resultadoBusca];
        $nome = readline("Digite o novo NOME ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Nome'] . " ]: ");
        $turma = readline("Digite a nova TURMA ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Turma'] . " ]: ");
        $curso = readline("Digite o novo CURSO ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Curso'] . " ]: ");
        $mensalidade = readline("Digite a nova MENSALIDADE ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Mensalidade'] . " ]: ");

        $AlunosMemory[$resultadoBusca]['Nome'] = $nome != "" ? $nome : $dadosAntigos['Nome'];
        $AlunosMemory[$resultadoBusca]['Turma'] = $turma != "" ? $turma : $dadosAntigos['Turma'];
        $AlunosMemory[$resultadoBusca]['Curso'] = $curso != "" ? $curso : $dadosAntigos['Curso'];
        $AlunosMemory[$resultadoBusca]['Mensalidade'] = $mensalidade != "" ? $mensalidade : $dadosAntigos['Mensalidade'];
        echo "Registro atualizado com sucesso !!" . PHP_EOL;
        readline("Click na tecla 'Enter' para continuar...");
    }
}

function MenuAlterar_prof()
{
    global $ProfessorMemory;
    echo "===Menu Alterar Professor===" . PHP_EOL;
    $nomeExclusão = readline("Digite o nome do professor para alteração: ");
    $resultadoBusca = pegarIndiceProfessorArrayPeloNome($nomeExclusão);
    if ($resultadoBusca == -1) {
        echo "!!!!!  Nome Invalido !!!!!" . PHP_EOL;
        readline("Click na tecla 'Enter' para continuar...");
    } else {
        popen('cls', 'w');
        $dadosAntigos = $ProfessorMemory[$resultadoBusca];
        $nome = readline("Digite o novo NOME ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Nome_prof'] . " ]: ");
        $salario = readline("Digite o novo SALARIO ou enter para permanecer o antigo [Antigo: " . $dadosAntigos['Salario'] . " ]: ");

        $ProfessorMemory[$resultadoBusca]['Nome_prof'] = $nome != "" ? $nome : $dadosAntigos['Nome_prof'];
        $ProfessorMemory[$resultadoBusca]['Salario'] = $salario != "" ? $salario : $dadosAntigos['Salario'];
        echo "Registro atualizado com sucesso !!" . PHP_EOL;
        $enter = readline("Click na tecla 'Enter' para continuar...");
        if ($enter != null) {
            echo "Isso não é uma opção invalida" . PHP_EOL;
            exit;
        }
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
        case 5:
            MenuCadst_prof();
            break;
        case 6:
            MenuListar_prof();
            break;
        case 7:
            MenuExcluir_prof();
            break;
        case 8:
            MenuAlterar_prof();
            break;
        case 9:
            calcularSalarioProf();
            break;
        case 10:
            exit;
        default:
            echo "Erro cód - 001: Não deveria chegar aqui o código" . PHP_EOL;
            break;
    }
}

function calcularSalarioProf()
{
    global $AlunosMemory;
    foreach ($AlunosMemory as $aluno) {
        global $mensalidadetotal;
        $mensalidadeint = intval($aluno['Mensalidade']);
        $mensalidadetotal += $mensalidadeint;
    }
    echo 'Mensalidade total apartir do número de alunos cadastrados: R$' . $mensalidadetotal . PHP_EOL;
    echo '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' . PHP_EOL;
    global $ProfessorMemory;
    foreach ($ProfessorMemory as $professor) {
        global $salariototal;
        $salarioint = intval($professor['Salario']);
        $salariototal += $salarioint;
    }
    echo 'Salario total apartir do número de professores cadastrados: R$' . $salariototal . PHP_EOL;
    echo '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' . PHP_EOL;
    if ($salariototal > $mensalidadetotal) {
        echo 'O salário dos professores é maior (ou igual) que a mensalidade dos alunos, não é possível pagar os professores!' . PHP_EOL;
    } else {
        echo 'A mensalidade dos alunos é maior (ou igual) que o salário dos professores, é possível pagar os professores!' . PHP_EOL;
    }
    readline("Click na tecla 'Enter' para continuar...");
}

while ($opcao != 10) {
    echo "====Menu====" . PHP_EOL;
    echo "1 - Cadastrar Aluno" . PHP_EOL;
    echo "2 - Listar os alunos" . PHP_EOL;
    echo "3 - Excluir Aluno" . PHP_EOL;
    echo "4 - Atualizar dados Aluno" . PHP_EOL;
    echo "5 - Cadastrar professor" . PHP_EOL;
    echo "6 - Listar os professor" . PHP_EOL;
    echo "7 - Excluir professor" . PHP_EOL;
    echo "8 - Atualizar dados professor" . PHP_EOL;
    echo "9 - Calcular salário dos professores" . PHP_EOL;
    echo "10 - Sair" . PHP_EOL;

    $opcao = readline("Digite sua opção: ");
    popen('cls', 'w');

    if (!in_array($opcao, $listaOpcoesValidas)) {
        echo "!!!!!  OPÇÃO INVALIDA  !!!!!" . PHP_EOL;
        readline("Click em qualquer tecla para continuar...");
    } else {
        verificarOpcaoMenu($opcao);
    }

    popen('cls', 'w');
}
