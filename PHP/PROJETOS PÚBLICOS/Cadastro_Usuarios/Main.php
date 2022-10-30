<?php

$lista;
$lista = [];
$value;

function menu(){ //----------------------------> -Função Principal- que contém todo o código.
   echo '++++ Menu ++++'. PHP_EOL; //--------------> Início do menu.
   echo PHP_EOL;
   echo '1. Cadastrar Usuário'. PHP_EOL;
   echo '2. Verificar Usuários'. PHP_EOL;
   echo '3. Remover Usuário'. PHP_EOL;
   echo '4. Sair';
   echo PHP_EOL;//--------------> Fim do menu.
   
   $lista;
   $opc_v = [1, 2, 3, 4]; //----------------------> Opções válidas. OBS: sempre que adicionar uma opção, adicione aqui também o seu valor para valida-lá.
   $opc = readline('Selecione uma opção: ');//------> Variável que recebe a -Opção- desejada.
   $lista = [];
   

   if($opc == 1){   //------> Faz checagem da -Opção-($opc) nas -Opções Válidas-($opc_v).
      $lista = [];
      $value = readline('Nome do Usuário: ');
      $lista[] = $value;   //---------------------------------> PROBLEMA: Não está adicionando usuários.
      menu();
   }if($opc == 2){  //---------------------> Exbibe usuários cadastrados.
      print_r($lista);
      menu();
      }elseif($opc == 3){ //-----------------> Remove usuário cadastrado. OBS: não foi testado devido o problema da 1 opção(Ln 23 to 25).
         $value = readline('Nome do Usuário: ');
         $search = array_search($value,$lista);
         if($search !== false){
         unset($lista[$search]);
         menu();
         }else{
            menu();
         }
      }if($opc == 4){ //----------------------------------> Fecha o programa inteiro.
         exit;
      }
}

menu(); //--------------------> Chama a -função Principal-(menu();) para o funcionamento do programa.